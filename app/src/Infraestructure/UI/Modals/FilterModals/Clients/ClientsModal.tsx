import "../ModalStyle.css";
import React, { useState, useEffect } from "react";
import "../ModalStyle.css";
import Search from "../TableSearchModals/TableSearchBar";
import { Users } from "./User";

export default function ClientsModal({ isOpen, toggleClientModal, selectedItems, setSelectedItems }: any) {
    const [activeComponent, setActiveComponent] = useState<'clientes' | 'rutas' | 'localidades' | 'jefatura' | 'gerencia' | 'canales' | 'cadena' |  'distribucion' | 'nivel' | 'exclusividad' | null>(null);
   
    
    const handleButtonClick = (component: 'clientes' | 'rutas' | 'localidades' | 'jefatura' | 'gerencia' | 'canales' | 'cadena' | 'distribucion' | 'nivel' | 'exclusividad') => {
        setActiveComponent(component); // Establece el componente activo según el botón presionado
    };

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
        toggleClientModal(); // Llama a la función para cerrar el modal
    }; 
    useEffect(() => {
        if (isOpen) {
            document.body.classList.add('active-modal'); 
        } else {
            document.body.classList.remove('active-modal');
        }
    }, [isOpen]);

    return (
        <>
            {isOpen && (
                <div className={"modal"}>
                    <div className={"overlay"}>
                        <div className={"modal-content"}>
                            <h2>CLIENTES</h2>
                            <hr className="divider" />
                            <a className={"transparent-text"}>
                                Aquí encontrarás todos los filtros para las características de clientes y estructura de
                                ventas
                            </a>
                            <hr className="divider" />
                            <div className={"modal-body"}>
                                <div className={"btn-container"}>
                                    <ul>
                                        <button onClick={() => handleButtonClick('clientes')}>Clientes</button>
                                        <button onClick={() => handleButtonClick('rutas')}>Rutas de ventas</button>
                                        <button onClick={() => handleButtonClick('localidades')}>Localidades de ventas</button>
                                        <button onClick={() => handleButtonClick('jefatura')}>Jefatura de venta</button>
                                        <button onClick={() => handleButtonClick('gerencia')}>Gerencia de zona</button>
                                        <button onClick={() => handleButtonClick('canales')}>Canales</button>
                                        <button onClick={() => handleButtonClick('cadena')}>Cadenas</button>
                                        <button onClick={() => handleButtonClick('distribucion')}>Sistema de distribucion</button>
                                        <button onClick={() => handleButtonClick('nivel')}>Nivel de vida</button>
                                        <button onClick={() => handleButtonClick('exclusividad')}>Exclusividad</button>
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