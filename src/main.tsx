import React, { useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import HomePage from "../src/Infraestructure/UI/HomePage/HomePage.tsx";
import LoginPage from "../src/Infraestructure/UI/LoginPage/LoginPage.tsx"
import MainMenuPage from './Infraestructure/UI/MainMenuPage/MainMenuPage.tsx';

const { BrowserRouter, Route, Switch, Link, Redirect } = window.ReactRouterDOM;

function App() {
    useEffect(() => {
    }, []);

    return (
        <BrowserRouter>
            <Switch>
                <Route exact path="/inicio" component={HomePage} />
                <Route exact path="/inicio/iniciar_Sesion" component={LoginPage} />
                <Route exact path="/inicio/acerca_de_vdv" component={HomePage} />
                <Route exact path="/main" component={MainMenuPage} />
                <Redirect to="/inicio" />
            </Switch>
        </BrowserRouter>
    );
}

// Renderizar la aplicación
ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);