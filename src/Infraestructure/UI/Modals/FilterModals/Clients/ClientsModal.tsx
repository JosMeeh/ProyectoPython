import "../ModalStyle.css";
import React, { useState, useEffect } from "react";
import Search from "../TableSearchModals/TableSearchBar";
import { apiRoutes } from "../../../../HTTPRoutes/apiRoutes";

export default function ClientsModal({ isOpen, toggleClientModal, selectedItems, setSelectedItems }) {
    const [activeComponent, setActiveComponent] = useState<'clientes' | 'rutas' | 'localidades' | 'jefatura' | 'gerencia' | 'canales' | 'cadena' | 'distribucion' | 'nivel' | 'exclusividad' | null>(null);
    const [componentData, setComponentData] = useState(null);
    const [loading, setLoading] = useState(false);
    const ApiRoutes = apiRoutes.get();

    const handleButtonClick = async (component: typeof activeComponent) => {
        setActiveComponent(component); // Set the active component based on the button clicked
        setLoading(true); // Start loading

        let newData = null;
        try {
            switch (component) {
                case 'clientes':
                    newData = await ApiRoutes.getData(); // Fetch data for clients
                    break;
                //case 'rutas':
                //    newData = await ApiRoutes.getRoutes(); // Fetch data for routes
                //    break;
                //case 'localidades':
                //    newData = await ApiRoutes.getLocalities(); // Fetch data for localities
                //    break;
                //case 'jefatura':
                //    newData = await ApiRoutes.getManagement(); // Fetch data for management
                //    break;
                //case 'gerencia':
                //    newData = await ApiRoutes.getZoneManagement(); // Fetch data for zone management
                //    break;
                //case 'canales':
                //    newData = await ApiRoutes.getChannels(); // Fetch data for channels
                //    break;
                //case 'cadena':
                //    newData = await ApiRoutes.getChains(); // Fetch data for chains
                //    break;
                //case 'distribucion':
                //    newData = await ApiRoutes.getDistribution(); // Fetch data for distribution
                //    break;
                //case 'nivel':
                //    newData = await ApiRoutes.getLifeLevel(); // Fetch data for life level
                //    break;
                //case 'exclusividad':
                //    newData = await ApiRoutes.getExclusivity(); // Fetch data for exclusivity
                //    break;
                default:
                    break;
            }
            setComponentData(newData.data.data);
        } catch (error) {
            console.error("Error fetching data:", error);
        } finally {
            setLoading(false); // Stop loading
        }
    };

    const handleCloseModal = () => {
        setActiveComponent(null); // Reset active component to null when closing modal
        toggleClientModal(); // Call function to close modal
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
                                Aquí encontrarás todos los filtros para las características de clientes y estructura de ventas.
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
                                {loading ? (
                                    <div>Loading...</div> // Show loading indicator while fetching data
                                ) : (
                                    activeComponent && componentData && (
                                        <Search selectedItems={selectedItems} setSelectedItems={setSelectedItems} data={componentData} />
                                    )
                                )}
                            </div>
                            <button className={"btn-close"} onClick={handleCloseModal}>X</button>
                        </div>
                    </div>
                </div>
            )}
        </>
    );
}