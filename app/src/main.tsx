import React, { useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom'; // Importing necessary components directly
import './index.css';
import Modal from "./Modal";
import  "react-datepicker/dist/react-datepicker.css"
import FilterMenu from "./FilterMenu";


function App() {
    useEffect(() => {
        // You can add any side effects here if needed
    }, []);

    return (
        // eslint-disable-next-line react/jsx-no-undef
        <FilterMenu/>
    );
}

// Renderizar la aplicación
ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);