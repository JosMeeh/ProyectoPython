import React, { useState } from "react";
import "./Modal.css";
import Search from "./TableSearchBar";
import {Users} from "./Users";

export default function Modal() {
    const [modal, setModal] = useState(false);
    const [activeComponent, setActiveComponent] = useState<'clientes' | 'rutas' | 'jefatura' | null>(null);
    const toggleModal = () => {
        setModal(!modal);
    };
    if (modal) {
        document.body.classList.add('active-modal');
    } else {
        document.body.classList.remove('active-modal');
    }
    const handleButtonClick = (component: 'clientes' | 'rutas' | 'jefatura') => {
        setActiveComponent(component); // Establece el componente activo según el botón presionado
    };
    const [selectedItems, setSelectedItems] = useState<any[]>([]); // Estado para los elementos seleccionados // Estado para los elementos seleccionados

    const renderActiveComponent = () => {
        switch (activeComponent) {
            case 'clientes':
                return <Search selectedItems={selectedItems} setSelectedItems={setSelectedItems} data={Users} />;
            // Agrega más casos según los componentes que necesites
            default:
                return null; // Retorna null si no hay componente activo
        }
    }
    const handleCloseModal = () => {
        setActiveComponent(null); // Restablece el componente activo a null al cerrar el modal
        toggleModal(); // Llama a la función para cerrar el modal
    };
    const print = () =>{
        console.log(selectedItems);
    }
    return (
        <>
            <button className={"btn-modal"} onClick={toggleModal}>open</button>
            <button className={"btn-modal"} onClick={print}>Print</button>
            {modal && (
                <div className={"modal"}>
                    <div className={"overlay"}>
                        <div className={"modal-content"}>
                            <h2>ATRIBUTOS DE CLIENTES</h2>
                            <hr className="divider"/>
                            <a className={"transparent-text"}>
                                Aquí encontrarás todos los filtros para las características de clientes y estructura de
                                ventas
                            </a>
                            <hr className="divider"/>
                            <div className={"modal-body"}>
                                <div className={"btn-container"}>
                                    <ul>
                                        <button onClick={() => handleButtonClick('clientes')}>Clientes</button>
                                        <button onClick={() => handleButtonClick('jefatura')}>Rutas de ventas</button>
                                        <button onClick={() => handleButtonClick('jefatura')}>Jefatura de venta</button>
                                        <button onClick={() => handleButtonClick('jefatura')}>Gerencia de zona</button>
                                        <button onClick={() => handleButtonClick('jefatura')}>Canales</button>
                                        <button onClick={() => handleButtonClick('jefatura')}>Cadenas</button>
                                        <button onClick={() => handleButtonClick('jefatura')}>Sistema de distribucion</button>
                                        <button onClick={() => handleButtonClick('jefatura')}>Nivel de vida</button>
                                        <button onClick={() => handleButtonClick('jefatura')}>Exclusividad</button>
                                    </ul>
                                </div>
                                {/* Renderiza el componente activo */}
                                {renderActiveComponent()}
                            </div>
                            <button className={"btn-close"} onClick={handleCloseModal}>X</button>
                        </div>
                    </div>
                </div>
            )}
        </>
    );
}