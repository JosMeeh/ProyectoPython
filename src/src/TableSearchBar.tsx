import React, { useState } from 'react';
import DataTable from './DataTable'; // Asegúrate de que este componente esté importado correctamente



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
            <input
                type="text"
                placeholder="Search..."
                className="search"
                onChange={(e) => setQuery(e.target.value)}
            />
            {/* Pasamos los datos filtrados a DataTable */}
            <DataTable
                data={search(data)}
                selectedItems={selectedItems}
                setSelectedItems={setSelectedItems}
            />
        </div>
    );
}