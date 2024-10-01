import {Users} from "./Users";
import React, { useState } from 'react';
import "./DataTable.css";

interface DataTableProps {
    selectedItems: any[];
    setSelectedItems: React.Dispatch<React.SetStateAction<any[]>>;
    data: any[];
}

export default function DataTable({ selectedItems, setSelectedItems, data }: DataTableProps) {
    const headers = Object.keys(data[0]);
    const handlePrint = (item: any) => {
        // Verificar si el item ya está en el array
        if (selectedItems.includes(item)) {
            // Si está, lo eliminamos
            const updatedItems = selectedItems.filter(selectedItem => selectedItem !== item);
            setSelectedItems(updatedItems);
            console.log(updatedItems); // Imprimir el array actualizado en consola
        } else {
            // Si no está, lo añadimos
            const updatedItems = [...selectedItems, item];
            setSelectedItems(updatedItems);
            console.log(updatedItems); // Imprimir el array actualizado en consola
        }
    }
    const handleSelectAll = () => {
        if (selectedItems.length === data.length) {
            // Si todos están seleccionados, deseleccionamos todos
            setSelectedItems([]);
            console.log([]); // Imprimir el array vacío en consola
        } else {
            // Si no todos están seleccionados, seleccionamos todos
            setSelectedItems(data);
            console.log(data); // Imprimir el array completo en consola
        }
    };
    return (
        <div className="table-container">
            <button onClick={handleSelectAll}>
                {selectedItems.length === data.length ? 'Deseleccionar Todos' : 'Seleccionar Todos'}
            </button>
            <table>
                <thead>
                <tr>
                    {headers.map((header : any) => (
                        <th key={header}>{header}</th>
                    ))}
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                {data.map((item : any, index : any) => (
                    <tr key={index}>
                        {headers.map((header) => (
                            <td key={header}>{item[header]}</td>
                        ))}
                        <td>
                            <button onClick={() => handlePrint(item)}>
                                {selectedItems.includes(item) ? 'Eliminar' : 'Agregar'}
                            </button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>
            <div>
            </div>
        </div>
    );
}