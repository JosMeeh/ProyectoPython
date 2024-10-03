import "../ModalStyle.css";
import React, { useState, useEffect } from "react";
import "../ModalStyle.css";
import Search from "../TableSearchModals/TableSearchBar";
import { DEENTREGAS } from "../DEntregas/DeEntregas";

export default function DeEntregasModal({ isOpen, toggleDeEntregasModal, selectedItems, setSelectedItems }: any) {
    const [activeComponent, setActiveComponent] = useState<'localidad' | 'ruta' | null>(null);


    const handleButtonClick = (component: 'localidad' | 'ruta') => {
        setActiveComponent(component); // Establece el componente activo según el botón presionado
    };

    const renderActiveComponent = () => {
          switch (activeComponent) {
              case 'localidad':
                  return <Search selectedItems={selectedItems} setSelectedItems={setSelectedItems} data={DEENTREGAS} />;
            // Agrega más casos según los componentes que necesites
            default:
                return null; // Retorna null si no hay componente activo
        }
    }
    const handleCloseModal = () => {
        setActiveComponent(null); // Restablece el componente activo a null al cerrar el modal
        toggleDeEntregasModal(); // Llama a la función para cerrar el modal
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
                            <h2>DETALLES DE ENTREGA</h2>
                            <hr className="divider" />
                            <a className={"transparent-text"}>
                                Aquí encontrarás todos los filtros para los detalles de entregas y localidades de liquidacion
                            </a>
                            <hr className="divider" />
                            <div className={"modal-body"}>
                                <div className={"btn-container"}>
                                    <ul>
                                        <button onClick={() => handleButtonClick('localidad')}>Localidad de liquidacion</button>
                                        <button onClick={() => handleButtonClick('ruta')}>Rutas de entregas</button>                                       
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