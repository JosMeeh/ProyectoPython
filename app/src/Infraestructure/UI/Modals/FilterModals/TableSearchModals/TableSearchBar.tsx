import React, { useState } from 'react';
import ModalDataTable from '../TableSearchModals/ModalDataTable/MDataTable'; // Asegúrate de que este componente esté importado correctamente
import "../TableSearchModals/TableSearchBar.css"


interface SearchProps {
    selectedItems: any[];
    setSelectedItems: React.Dispatch<React.SetStateAction<any[]>>;
    data: any[]; // Recibe los datos como prop
}

export default function Search({ selectedItems, setSelectedItems, data }: SearchProps) {
    const [query, setQuery] = useState("");

    const search = (data: any[]) => {
        if (!data || data.length === 0) return []; // Manejo de datos vacíos
        // Filtrar los datos según la consulta
        const filteredData = data.filter((item) => {
            const lowerCaseQuery = query.toLowerCase();
            return Object.values(item).some(value =>
                typeof value === 'string' && value.toLowerCase().includes(lowerCaseQuery)
            );
        });
        // Si no hay coincidencias, devolver todos los datos
        return filteredData.length > 0 ? filteredData : data;
    };

    return (
        <div className="table">
            <div className="search-container">
            <div className="search-bar-container">
                <i className='bx bx-search'></i>
            <input
                type="text"
                placeholder="Buscar..."
                className="search-bar"
                onChange={(e) => setQuery(e.target.value)}
                />
            </div>
            </div>
            {/* Pasamos los datos filtrados a DataTable */}
            <ModalDataTable
                data={search(data)}
                selectedItems={selectedItems}
                setSelectedItems={setSelectedItems}
            />
        </div>
    );
}