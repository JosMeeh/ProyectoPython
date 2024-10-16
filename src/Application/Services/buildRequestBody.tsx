import { IServices } from "../Interfaces/IServices";

// Definición de tipos
interface Cliente {
    CodigoCliente: number;
    NombreCliente: string;
}

interface Localidad {
    idLocalidad: string;
    "Localidad1": string;
}

interface Producto {
    sku: string;
    Descripcion: string;
}

interface Dates {
    start_date: string; // o Date si prefieres
    end_date: string; // o Date si prefieres
}

type DataItem = Cliente | Localidad | Producto | Dates;

interface FilterValue {
    column_name: string;
    value: string | number;
    operator: string;
}

interface Filter {
    colunm_select: string[];
    table_name: string;
    filter_values: FilterValue[];
}

interface Result {
    Filters: Filter[];
    Dates?: Dates;
}

export class buildRequestBody implements IServices<any, Result> {
    private result: Result;

    constructor() {
        this.result = { Filters: [] };
    }

    private addFilter(tableName: string, columnName: string, value: string | number, operator: string = "Equal") {
        // Verificar si ya existe un filtro para la tabla
        let filter = this.result.Filters.find(f => f.table_name === tableName);

        if (!filter) {
            // Si no existe, crear uno nuevo
            filter = {
                colunm_select: [],
                table_name: tableName,
                filter_values: []
            };
            this.result.Filters.push(filter);
        }

        // Agregar el nombre de la columna si no está ya en colunm_select
        if (!filter.colunm_select.includes(columnName)) {
            filter.colunm_select.push(columnName);
        }

        // Agregar el valor al filter_values
        filter.filter_values.push({
            column_name: columnName,
            value,
            operator
        });
    }

    private addDateFilter(tableName: string, startDate: string, endDate: string) {
        const filter = {
            colunm_select: ["fecha"],
            table_name: tableName,
            filter_values: [
                {
                    column_name: "fecha",
                    value: startDate,
                    operator: "greater_than"
                },
                {
                    column_name: "fecha",
                    value: endDate,
                    operator: "less_than"
                }
            ]
        };

        this.result.Filters.push(filter);
    }

    execute(data: any): Result {
        // Extraer fechas del objeto data si están presentes
        const Dates = data.find((item: any) => 'start_date' in item && 'end_date' in item) as Dates;

        if (Dates) {
            this.addDateFilter("Tabla_Fechas", Dates.start_date, Dates.end_date);
        }

        // Transformación de los datos originales
        data.forEach((item: any) => {
            if ('CodigoCliente' in item) {
                this.addFilter("Clientes", "Nombre_Cliente", item.NombreCliente.trim());
            } else if ('Loc' in item) {
                this.addFilter("Localidad", "Localidad", item["Localidad1"].trim());
            } else if ('sku' in item) {
                this.addFilter("Tabla_Productos", "sku", item.sku);
                this.addFilter("Tabla_Productos", "Descripcion", item.Descripcion.trim());
            }
        });

        return this.result;
    }

    static get(): IServices<any, Result> {
        return new buildRequestBody();
    }
}