import {Users} from "./Users";
import React, {useEffect, useState} from 'react';
import "./DataTable.css";
import  "./filtermenu.css";
import  "react-datepicker/dist/react-datepicker.css"
import DatePicker from "react-datepicker";
import Modal from "./Modal";
import MenuOfFilters from "./MenuOfFilters";

export default function FilterMenu(){

    const [showDataTable, setShowDataTable] = useState(false);
    const [isModalOpen, setIsModalOpen] = useState(false); // Estado para controlar el modal
    const handleOptionClick = () => {
        setShowDataTable(true);
    };
    const toggleModal = () => {
        setIsModalOpen(!isModalOpen); // Cambia el estado del modal
    };
    useEffect(() => {
        const btn = document.getElementById("btn");
        const sidebar = document.getElementsByClassName("Sidebar")[0];

        if (btn && sidebar) {
            btn.onclick = function () {
                sidebar.classList.toggle("active");
            }
        }
    }, []);

    return (
        <div>
            <div className="Sidebar">
                <div className="Logo_content">
                    <div className="Logo">
                        <i className='bx bx-bar-chart-alt'></i>
                        <div className="Logo_name">Visualizador dinamico</div>
                    </div>
                    <i className='bx bx-menu' id="btn"></i>
                    <ul className="nav_list">
                        <li>
                            <a href="#" onClick={() => handleOptionClick()}>
                                <i className='bx bxs-grid-alt bx-flip-vertical'></i>
                                <span className="links_name">Inicio </span>
                            </a>
                            <span className="tooltip">Inicio </span>
                        </li>
                        <li>
                            <a href="#" onClick={toggleModal}>
                                <i className='bx bx-package'></i>
                                <span className="links_name">Consultas</span>
                            </a>
                            <span className="tooltip">Consultas </span>
                        </li>
                        <li>
                            <a href="#">
                                <i className='bx bxs-report'></i>
                                <span className="links_name">Reportes </span>
                            </a>
                            <span className="tooltip">Reportes </span>
                        </li>
                        <li>
                            <a href="#">
                                <i className='bx bxs-cog'></i>
                                <span className="links_name">Configuracion </span>
                            </a>
                            <span className="tooltip">Configuracion </span>
                        </li>
                        <li>
                            <a href="#"> {/*Los onclick aqui*/}
                                <i className='bx bxs-log-out' id="log_out"></i>
                                <span  className="links_name">Salir </span>
                            </a>
                            <span className="tooltip">Salir </span>
                        </li>
                    </ul>
                </div>
                <Modal isOpen={isModalOpen} toggleModal={toggleModal} />
            </div>
            <div className="Home_content">
                <MenuOfFilters/>
            </div>
        </div>
    );
}