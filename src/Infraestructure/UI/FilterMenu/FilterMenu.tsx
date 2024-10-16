import React, { useState } from 'react';
import "./FilterMenu.css";
import ClientsModal from '../Modals/FilterModals/Clients/ClientsModal';
import SkuModal from '../Modals/FilterModals/Sku/SkuModal';
import DeEntregasModal from '../Modals/FilterModals/DEntregas/DEntregasModal';
import DataTableContainer from '../MainMenuPage/Datatable/DataTableComponent';
import { buildRequestBody } from "../../../Application/Services/buildRequestBody"

export default function FilterMenu() {
    //TABLA DE RESULTADOS
    const [showDataTable, setShowDataTable] = useState(false);
    const [jsonRequest, setjsonRequest] = useState<any>();
    const handleOptionClick = () => {
        const buildRequest: buildRequestBody = buildRequestBody.get();
        const Dates = {
            "start_date": startDate,
            "end_date": endDate
        };

        const updatedSelectedItems = [...selectedItems, Dates];
        const result = buildRequest.execute(updatedSelectedItems);
        console.log(result);
        setjsonRequest(result);
        setShowDataTable(true); // Descomenta si es necesario
    };
    //CONSTANTES PARA EL CONTROL DE LOS MODALS
    const [isClientsModalOpen, setIsClientsModalOpen] = useState(false); 
    const [isSkuModalOpen, setIsSkuModalOpen] = useState(false);
    const [isDeEntregasOpen, setIsDeEntregasModalOpen] = useState(false);
    //FUNCIONES PARA APERTURA DE MODALS
    const toggleClientModal = () => {
        setIsClientsModalOpen(!isClientsModalOpen); 
    };
    const toggleSkuModal = () => {
        setIsSkuModalOpen(!isSkuModalOpen);
        if (isClientsModalOpen || isDeEntregasOpen) { setIsClientsModalOpen(false); setIsDeEntregasModalOpen(false); } // Close Clients modal if it's open
    };
    const toggleDeEntregasModal = () => {
        setIsDeEntregasModalOpen(!isDeEntregasOpen);
        if (isClientsModalOpen || isSkuModalOpen) { setIsClientsModalOpen(false); setIsSkuModalOpen(false); } // Close Clients modal if it's open
    };
    // Estado para los elementos seleccionados
    const [selectedItems, setSelectedItems] = useState<any[]>([]);  
    // CONTROL DEL CALENDARIO
    const [startDate, setStartDate] = useState<string>('');
    const [endDate, setEndDate] = useState<string>('');
    const minDate = new Date(2002, 0, 1).toISOString().split('T')[0];
    const maxDate = new Date().toISOString().split('T')[0]; 
    const areDatesSelected = startDate && endDate; // Verifica si se han seleccionado fechas

    return (
        <div> 
        <div className="menuOfFilters">
            <label className="mainLable">Menu de consultas</label>
            <hr className="divider" />
            <div className="contenedor">
                <div className="date-pickers">
                    <label>Fecha de Inicio:</label>
                    <input
                        type="date"
                        value={startDate}
                        onChange={(e) => setStartDate(e.target.value)}
                        min={minDate} // Establece la fecha mínima
                        max={maxDate} // Establece la fecha máxima
                        aria-label="Seleccionar Fecha de Inicio"
                    />

                    <label>Fecha de Fin:</label>
                    <input
                        type="date"
                        value={endDate}
                        onChange={(e) => {
                            // Solo permite seleccionar fechas que no sean anteriores a la fecha de inicio
                            if (!startDate || e.target.value >= startDate) {
                                setEndDate(e.target.value);
                            }
                        }}
                        min={startDate || minDate} // Establece la fecha mínima como la fecha de inicio o el mínimo permitido
                        max={maxDate} // Establece la fecha máxima
                        aria-label="Seleccionar Fecha de Fin"
                    />
                </div>
                <hr className="divider" />
                <label className="filterLable">Filtros:</label>
                <ul className={"nav-list-menu"}>
                    <hr className="divider" />
                    <li>
                        <a href="#" onClick={areDatesSelected ? toggleClientModal : undefined} style={{ pointerEvents: areDatesSelected ? 'auto' : 'none', opacity: areDatesSelected ? 1 : 0.5 }}>
                            <i className='bx bxs-chevron-down'></i>
                            <span className="links_name">Clientes</span>
                        </a>
                    </li>
                    <hr className="divider" />
                    <li>
                        <a href="#" onClick={areDatesSelected ? toggleSkuModal : undefined} style={{ pointerEvents: areDatesSelected ? 'auto' : 'none', opacity: areDatesSelected ? 1 : 0.5 }}>
                            <i className='bx bxs-chevron-down'></i>
                            <span className="links_name">Productos</span>
                        </a>
                    </li>
                    <hr className="divider" />
                    <li>
                        <a href="#" onClick={areDatesSelected ? toggleDeEntregasModal : undefined} style={{ pointerEvents: areDatesSelected ? 'auto' : 'none', opacity: areDatesSelected ? 1 : 0.5 }}>
                            <i className='bx bxs-chevron-down'></i>
                            <span className="links_name">Datos de entrega</span>
                        </a>
                    </li>
                    <hr className="divider" />
                    <li>
                        <a href="#" style={{ pointerEvents: areDatesSelected ? 'auto' : 'none', opacity: areDatesSelected ? 1 : 0.5 }}>
                            <i className='bx bxs-chevron-down'></i>
                            <span className="links_name">Indicadores</span>
                        </a>
                    </li>
                    <hr className="divider" />
                </ul>
                <button className="filterMenuButton" onClick={handleOptionClick} disabled={!areDatesSelected} style={{ opacity: areDatesSelected ? 1 : 0.5 }}> Aplicar filtros </button>
                </div>
            {/* Modal para atributos de clientes */}
            </div>
            <div className="Home_content_Filter">
                {/*<div className="text">*/}
                {/*    <li>Selecciona un rango de fechas para realizar una consulta.</li>*/}
                {/*    <li>Puedes seleccionar filtros para hacer tu consulta mas precisa.</li>*/}
                {/*</div>*/}
                <ClientsModal isOpen={isClientsModalOpen} toggleClientModal={toggleClientModal} selectedItems={selectedItems} setSelectedItems={setSelectedItems} />
                <SkuModal isOpen={isSkuModalOpen} toggleSkuModal={toggleSkuModal} selectedItems={selectedItems} setSelectedItems={setSelectedItems} />
                <DeEntregasModal isOpen={isDeEntregasOpen} toggleDeEntregasModal={toggleDeEntregasModal} selectedItems={selectedItems} setSelectedItems={setSelectedItems} />

                <div className="data-table-wrapper">
                    {showDataTable && <DataTableContainer parameters={jsonRequest} />}
                </div>
            </div>
            {/* Mensaje informativo */}
        </div>
    );
}