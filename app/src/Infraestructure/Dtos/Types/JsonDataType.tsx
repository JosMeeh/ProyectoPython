export type JsonData = {
    statusCode: number;
    message: string;
    data: Array<Record<string, any>>;
};

export type DataTableColumn = {
    title: string;                       // T�tulo de la columna
    data: string;                        // Clave del objeto que corresponde a esta columna
};

// Define un tipo para la configuraci�n de la tabla
export type DataTableConfig = {
    columns: Array<DataTableColumn>;     // Array de columnas
    data: Array<Record<string, any>>;     // Datos de la tabla, donde los valores pueden ser de cualquier tipo
    totalRecords: number;                 // Total de registros disponibles
    currentPage: number;                  // P�gina actual
    totalPages: number;                   // Total de p�ginas disponibles
};