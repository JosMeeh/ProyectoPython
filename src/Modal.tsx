import React, { useState } from "react";
import "./Modal.css";
import Search from "./TableSearchBar";

export default function Modal() {
    const [modal, setModal] = useState(false);
    const toggleModal = () => {
        setModal(!modal);
    };
    const print = () => {
        console.log("Pedro");
    };

    if (modal) {
        document.body.classList.add('active-modal');
    } else {
        document.body.classList.remove('active-modal');
    }

    return (
        <>
            <button className={"btn-modal"} onClick={toggleModal}>open</button>
            {modal && (
                <div className={"modal"}>
                    <div className={"overlay"}>
                        <div className={"modal-content"}>
                            <h2>ATRIBUTOS DE CLIENTES</h2>
                            <hr className="divider" />
                            <a className={"transparent-text"}>
                                Aquí encontrarás todos los filtros para las características de clientes y estructura de ventas
                            </a>
                            <hr className="divider" />
                            <div className={"modal-body"}>
                                <div className={"btn-container"}>
                                    <ul>
                                        <button onClick={(e) => {
                                            print();
                                        }}>Clientes
                                        </button>
                                        <button onClick={(e) => {
                                            print();
                                        }}>Rutas de ventas
                                        </button>
                                        <button onClick={(e) => {
                                            print();
                                        }}>Jefatura de venta
                                        </button>
                                        <button onClick={(e) => {
                                            print();
                                        }}>Gerencia de zona
                                        </button>
                                        <button onClick={(e) => {
                                            print();
                                        }}>Canales
                                        </button>
                                        <button onClick={(e) => {
                                            print();
                                        }}>Cadenas
                                        </button>
                                        <button onClick={(e) => {
                                            print();
                                        }}>Sistema de distribucion
                                        </button>
                                        <button onClick={(e) => {
                                            print();
                                        }}>Nivel de vida
                                        </button>
                                        <button onClick={(e) => {
                                            print();
                                        }}>Exclusividad
                                        </button>
                                    </ul>
                                </div>
                                <div className={"search-bar-container"}>
                                    <Search/>
                                </div>
                            </div>
                            <button className={"btn-close"} onClick={toggleModal}>X</button>
                        </div>
                    </div>
                </div>
            )}
        </>
    );
}