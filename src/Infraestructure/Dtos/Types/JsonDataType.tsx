export type JsonData = {
    statusCode: number;
    message: string;
    data: Array<Record<string, any>>;
};

export type DataTableColumn = {
    title: string;
    data: string;
};

export type DataTableConfig = {
    columns: Array<DataTableColumn>;
    data: Array<Record<string, any>>;
};