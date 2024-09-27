import React, { useEffect, useState } from 'react';
import { buildDatatable } from "../../../../Application/Services/buildDatatable";
import DataTable from "../Datatable/DataTable";

export default function DataTableContainer({ parameters }) {
    const [dataTableData, setDataTableData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [currentPage, setCurrentPage] = useState(1); // Estado para la página actual
    const databuild = buildDatatable.get();

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            setError(null);
            try {
                const result = await databuild.execute(parameters);
                if (result) {
                    setDataTableData(result);
                } else {
                    setError('No data available');
                }
            } catch (err) {
                console.error('Error executing data build:', err);
                setError('Error loading data');
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [parameters]);

    // Parámetros de paginación
    const pageSize = 100;
    const startIndex = (currentPage - 1) * pageSize;
    const endIndex = startIndex + pageSize;
    const paginatedData = dataTableData ? dataTableData.data.slice(startIndex, endIndex) : [];

    return (
        <div>
            {loading && <div>Cargando datos...</div>}
            {error && <div>{error}</div>}
            {dataTableData && (
                <>
                    <DataTable
                        columns={dataTableData.columns}
                        data={paginatedData}
                    />
                    <div>
                        <button onClick={() => setCurrentPage(currentPage - 1)} disabled={currentPage === 1}>
                            Anterior
                        </button>
                        <span>Página {currentPage} de {dataTableData.totalPages}</span>
                        <button onClick={() => setCurrentPage(currentPage + 1)} disabled={currentPage === dataTableData.totalPages}>
                            Siguiente
                        </button>
                    </div>
                </>
            )}
        </div>
    );
}