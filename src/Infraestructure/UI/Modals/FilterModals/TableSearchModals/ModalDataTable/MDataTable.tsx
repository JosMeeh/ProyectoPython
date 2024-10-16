import React, { useState } from 'react';
import "./ModalDataTable.css";

interface DataTableProps {
    selectedItems: any[];
    setSelectedItems: React.Dispatch<React.SetStateAction<any[]>>;
    data: any[];
}

export default function DataTable({ selectedItems, setSelectedItems, data }: DataTableProps) {
    const [currentPage, setCurrentPage] = useState(0);
    const itemsPerPage = 10; // Define how many items per page
    const headers = Object.keys(data[0]);

    const handlePrint = (item: any) => {
        if (selectedItems.includes(item)) {
            const updatedItems = selectedItems.filter(selectedItem => selectedItem !== item);
            setSelectedItems(updatedItems);
        } else {
            const updatedItems = [...selectedItems, item];
            setSelectedItems(updatedItems);
        }
    };

    const handleSelectAll = () => {
        if (selectedItems.length === data.length) {
            setSelectedItems([]);
        } else {
            setSelectedItems(data);
        }
    };

    // Calculate the current items for the current page
    const currentData = data.slice(currentPage * itemsPerPage, (currentPage + 1) * itemsPerPage);
    const totalPages = Math.ceil(data.length / itemsPerPage);

    // Pagination handlers
    const nextPage = () => {
        if (currentPage < totalPages - 1) {
            setCurrentPage(prev => prev + 1);
        }
    };

    const prevPage = () => {
        if (currentPage > 0) {
            setCurrentPage(prev => prev - 1);
        }
    };

    return (
        <div className="table-container">
            <button className={"select-all-button"} onClick={handleSelectAll}>
                {selectedItems.length === data.length ? 'Deseleccionar Todos' : 'Seleccionar Todos'}
            </button>
            <table>
                <thead>
                    <tr>
                        {headers.map((header: any) => (
                            <th key={header}>{header}</th>
                        ))}
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {currentData.map((item: any, index: any) => (
                        <tr key={index}>
                            {headers.map((header) => (
                                <td key={header}>{item[header]}</td>
                            ))}
                            <td>
                                <button className={"table_button"} onClick={() => handlePrint(item)}>
                                    {selectedItems.includes(item) ? 'Eliminar' : 'Agregar'}
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {/* Pagination Controls */}
            <div className="pagination-controls">
                <button onClick={prevPage} disabled={currentPage === 0}>Anterior</button>
                <span>Página {currentPage + 1} de {totalPages}</span>
                <button onClick={nextPage} disabled={currentPage === totalPages - 1}>Siguiente</button>
            </div>
        </div>
    );
}