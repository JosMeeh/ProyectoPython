import "../ModalStyle.css";
import React, { useState, useEffect } from "react";
import "../ModalStyle.css";
import Search from "../TableSearchModals/TableSearchBar";
import { SKU } from "../Sku/sku";

export default function SkuModal({ isOpen, toggleSkuModal, selectedItems, setSelectedItems }: any) {
    const [activeComponent, setActiveComponent] = useState<'sku' | 'tipo' | 'categoria' | 'marca' | 'tamano' | 'retornabilidad' | 'sabor' | 'empaque' | 'presentacion' | null>(null);


    const handleButtonClick = (component: 'sku' | 'tipo' | 'categoria' | 'marca' | 'tamano' | 'retornabilidad' | 'sabor' | 'empaque' | 'presentacion') => {
        setActiveComponent(component); // Establece el componente activo según el botón presionado
    };

    const renderActiveComponent = () => {
        switch (activeComponent) {
            case 'sku':
                return <Search selectedItems={selectedItems} setSelectedItems={setSelectedItems} data={SKU} />;
            // Agrega más casos según los componentes que necesites
            default:
                return null; // Retorna null si no hay componente activo
        }
    }
    const handleCloseModal = () => {
        setActiveComponent(null); // Restablece el componente activo a null al cerrar el modal
        toggleSkuModal(); // Llama a la función para cerrar el modal
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
                            <h2>PRODUCTOS</h2>
                            <hr className="divider" />
                            <a className={"transparent-text"}>
                                Aquí encontrarás todos los filtros para las características de productos
                                ventas
                            </a>
                            <hr className="divider" />
                            <div className={"modal-body"}>
                                <div className={"btn-container"}>
                                    <ul>
                                        <button onClick={() => handleButtonClick('sku')}>SKU S</button>
                                        <button onClick={() => handleButtonClick('tipo')}>Tipo de producto</button>
                                        <button onClick={() => handleButtonClick('categoria')}>Categoria</button>
                                        <button onClick={() => handleButtonClick('marca')}>Marca</button>
                                        <button onClick={() => handleButtonClick('tamano')}>Tamano</button>
                                        <button onClick={() => handleButtonClick('retornabilidad')}>Retornabilidad</button>
                                        <button onClick={() => handleButtonClick('sabor')}>Sabor</button>
                                        <button onClick={() => handleButtonClick('empaque')}>Empaque</button>
                                        <button onClick={() => handleButtonClick('presentacion')}>Presentacion</button>
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