import {Users} from "./Users";

import React from 'react';
import "./DataTable.css";


export default function DataTable({ data }: any) {
    return (
        <div className="table-container">
            <table>
                <thead>
                <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Options</th>
                </tr>
                </thead>
                <tbody>
                {data.map((item: any) => (
                    <tr key={item.Id}> {/* Usando item.Id como clave */}
                        <td>{item.Id}</td>
                        {/* Asumiendo que id existe */}
                        <td>{item.Name}</td>
                        {/* Asumiendo que name existe */}
                        <td>{item.Type}</td>
                        {/* Asumiendo que type existe */}
                        <td>
                            <button>acción</button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}