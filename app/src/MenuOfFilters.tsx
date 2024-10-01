import React, { useState } from 'react';
import "./MenuOfFilters.css";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

/* PARA AGREGAR EN EL PROYECTO
* <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/react-datepicker/4.0.0/react-datepicker.min.css" />
<script src="https://unpkg.com/react/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom/umd/react-dom.development.js" crossorigin></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-datepicker/4.0.0/react-datepicker.min.js"></script>
<script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
* */

export default function MenuOfFilters() {
    const [startDate, setStartDate] = useState<Date | null>(new Date());
    const [endDate, setEndDate] = useState<Date | null>(new Date());

    // Fecha mínima: 1 de enero de 2002
    const minDate = new Date(2002, 0, 1);
    // Fecha máxima: fecha actual
    const maxDate = new Date();

    return (
        <div className="menuOfFilters">
            <div className="contenedor">
                <div className="date-pickers">
                    <label>Fecha de Inicio:</label>
                    <DatePicker
                        selected={startDate}
                        onChange={(date) => setStartDate(date)}
                        dateFormat="dd/MM/yyyy"
                        minDate={minDate} // Establece la fecha mínima
                        maxDate={maxDate} // Establece la fecha máxima (hoy)
                        showMonthYearDropdown // Muestra el menú desplegable para mes y año
                        dropdownMode="select" // Cambia a modo de selección para el desplegable
                    />

                    <label>Fecha de Fin:</label>
                    <DatePicker
                        selected={endDate}
                        onChange={(date) => setEndDate(date)}
                        dateFormat="dd/MM/yyyy"
                        minDate={startDate ? startDate : minDate} // Asegura que no se pueda seleccionar una fecha anterior a la de inicio
                        maxDate={maxDate} // Establece la fecha máxima (hoy)
                        showMonthYearDropdown // Muestra el menú desplegable para mes y año
                        dropdownMode="select" // Cambia a modo de selección para el desplegable
                    />
                </div>
                <ul className={"nav-list-menu"}>
                    <hr className="divider"/>
                    <li>
                        <a href="#">
                            <i className='bx bxs-chevron-down'></i>
                            <span className="links_name">Atributos de clientes</span>
                        </a>
                    </li>
                    <hr className="divider"/>
                    <li>
                        <a href="#">
                            <i className='bx bxs-chevron-down'></i>
                            <span className="links_name">Atributos de SKU</span>
                        </a>
                    </li>
                    <hr className="divider"/>
                    <li>
                        <a href="#">
                            <i className='bx bxs-chevron-down'></i>
                            <span className="links_name">Datos de entrega</span>
                        </a>
                    </li>
                    <hr className="divider"/>
                    <li>
                        <a href="#">
                            <i className='bx bxs-chevron-down'></i>
                            <span className="links_name">Indicadores</span>
                        </a>
                    </li>
                    <hr className="divider"/>
                </ul>
            </div>
        </div>
    );
}