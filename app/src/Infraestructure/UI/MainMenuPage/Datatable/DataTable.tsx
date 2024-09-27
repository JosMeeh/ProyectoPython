import { DataTableConfig, DataTableColumn } from "../../../Dtos/Types/JsonDataType";
import "../Datatable/DataTable.css";

const DataTable: React.FC<DataTableConfig> = ({ columns, data }) => {
    return (
        <div className="data-table-container">
            <table className="data-table">
                <thead>
                    <tr>
                        {columns.map((column) => (
                            <th key={column.data} className="data-table-header">
                                {column.title}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {data.length > 0 ? (
                        data.map((row, index) => (
                            <tr key={index} className="data-table-row">
                                {columns.map((column) => (
                                    <td key={column.data} className="data-table-cell">
                                        {row[column.data] !== undefined ? row[column.data] : 'N/A'}
                                    </td>
                                ))}
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan={columns.length} className="data-table-cell no-data">
                                No data available
                            </td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default DataTable;