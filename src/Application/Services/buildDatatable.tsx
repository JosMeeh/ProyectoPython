import { DataTableColumn, DataTableConfig } from "../../Infraestructure/Dtos/Types/JsonDataType";
import { apiRoutes } from "../../Infraestructure/HTTPRoutes/apiRoutes";
import { IServices } from "../Interfaces/IServices";

export class buildDatatable implements IServices<string, Promise<DataTableConfig | null>> {
    apiRoute: apiRoutes = apiRoutes.get();

    async execute(parameters: string): Promise<DataTableConfig | null> {
        const response = await this.apiRoute.dynamicConsult(parameters);
        if (response) {
            try {
                const dataArray = response.data.data; // Accede al campo "data"
                console.log('Data Array Length:', dataArray.length); // Verifica el tamaño de los datos

                if (!dataArray || dataArray.length === 0) {
                    return null; // Retornar null si no hay datos
                }

                // Obtener las claves únicas de todos los objetos, omitiendo los valores nulos
                const allKeys = new Set<string>();
                for (const item of dataArray) {
                    if (item && typeof item === 'object') { // Asegurarse de que item es un objeto
                        Object.keys(item).forEach((key) => {
                            if (item[key] !== null && item[key] !== undefined) { // Solo añadir claves con valores no nulos o indefinidos
                                allKeys.add(key);
                            }
                        });
                    }
                }

                // Crear las columnas solo para claves que tienen valores no nulos
                const columns: Array<DataTableColumn> = Array.from(allKeys).map((key) => ({
                    title: key.trim(), // Elimina espacios en blanco
                    data: key.trim(),
                }));

                // Crear los datos para la tabla, omitiendo valores nulos y convirtiendo booleanos a "Sí" y "No"
                const data: Array<Record<string, any>> = [];
                for (const item of dataArray) {
                    if (item && typeof item === 'object') { // Asegurarse de que item es un objeto
                        const rowData: Record<string, any> = {};
                        for (const key of allKeys) {
                            const value = item[key];
                            if (value !== null && value !== undefined) { // Solo asignar valores no nulos e indefinidos
                                if (typeof value === 'boolean') {
                                    rowData[key] = value ? 'Si' : 'No'; // Convertir booleanos a "Sí" o "No"
                                } else if (typeof value === 'string' || typeof value === 'number') {
                                    rowData[key] = value; // Asignar cadenas y números directamente
                                } else {
                                    console.warn(`Valor no renderizable encontrado en ${key}:`, value); // Advertencia para otros tipos
                                }
                            }
                        }
                        if (Object.keys(rowData).length > 0) { // Solo agregar filas no vacías
                            data.push(rowData);
                        }
                    }
                }

                return {
                    columns,
                    data,
                    totalRecords: dataArray.length, // Total de registros para manejar la paginación en el frontend
                    currentPage: 1, // Establecer la página actual en 1, ya que se manejará localmente
                    totalPages: Math.ceil(dataArray.length / 100), // Calcular total de páginas basado en el tamaño total
                };
            } catch (error) {
                console.error('Error al cargar los datos:', error);
                return null; // Manejo de errores
            }
        }
        return null;
    }

    static get(): IServices<string, Promise<DataTableConfig | null>> {
        return new buildDatatable();
    }
}