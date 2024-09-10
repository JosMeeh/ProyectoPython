import { DataTableColumn, DataTableConfig } from "../../Infraestructure/Dtos/Types/JsonDataType";
import { apiRoutes } from "../../Infraestructure/HTTPRoutes/apiRoutes";
import { IServices } from "../Interfaces/IServices";

export class buildDatatable implements IServices<string, Promise<DataTableConfig | null>> {
    apiRoute: apiRoutes = apiRoutes.get();
    async execute(parameters: string): Promise<DataTableConfig | null> {
        const response = await this.apiRoute.dynamicConsult();
        if (response) {
            try {
                const dataArray = response.data.data; // Accede al campo "data"
                console.log('Data Array Length:', dataArray.length); // Verifica el tamaño de los datos

                if (!dataArray || dataArray.length === 0) {
                    return null; // Retornar null si no hay datos
                }

                // Obtener las claves únicas de todos los objetos, omitiendo los valores nulos
                const allKeys = new Map<string, boolean>();
                for (const item of dataArray) {
                    if (item && typeof item === 'object') { // Asegurarse de que item es un objeto
                        Object.keys(item).forEach((key) => {
                            if (item[key] !== null) { // Solo añadir claves con valores no nulos
                                allKeys.set(key, true);
                            }
                        });
                    }
                }

                // Crear las columnas solo para claves que tienen valores no nulos
                const columns: Array<DataTableColumn> = Array.from(allKeys.keys()).map((key) => ({
                    title: key,
                    data: key,
                }));

                // Crear los datos para la tabla, omitiendo valores nulos y convirtiendo booleanos a "Sí" y "No"
                const data: Array<Record<string, any>> = [];
                for (const item of dataArray) {
                    if (item && typeof item === 'object') { // Asegurarse de que item es un objeto
                        const rowData: Record<string, any> = {};
                        for (const key of allKeys.keys()) {
                            if (item[key] !== null) { // Solo asignar valores no nulos
                                rowData[key] = typeof item[key] === 'boolean' ? (item[key] ? 'Si' : 'No') : item[key];
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
                };
            } catch (error) {
                console.error('Error al cargar los datos:', error);
                return null; // Manejo de errores
            }
        }
        return null;
    }




    static get(): IServices<string, Promise<DataTableConfig | null>> {
        return new buildDatatable;
    }



}