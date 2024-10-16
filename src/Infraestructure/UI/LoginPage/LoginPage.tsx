import { urlTraveler } from "../../../Application/Services/urlTraveler"
import "./LoginPage.css"
import "../Components/sharedStyles.css"
import React, { useState } from 'react';
import { catchLogin } from "../../../Application/Services/catchLogin";
import { ResponseBody } from "../../Dtos/ResponseBody";
import { AuthUserResponse } from "../../Dtos/AuthUserResponse";



export default function LoginPage() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const urlTravel = urlTraveler.get();
    const login = catchLogin.get();
    const [errorMessage, setErrorMessage] = useState(''); // Estado para el mensaje de error
    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault(); 
        const userData = [username, password];
        const response: ResponseBody<AuthUserResponse> = await login.execute(userData);
        if (response.Getresponse_code == 200) {
            console.log("Welcome to new VDV")
            urlTravel.execute("/main");
        } else if (response.Getresponse_code == 401) {
            setPassword('');
            setErrorMessage(response.Getresponse_message);
        } else {
            setUsername('');
            setPassword('');
            setErrorMessage(response.Getresponse_message)
        };
        
    };
    return (
        <div className= "full-homepage">
            <header className="header-homepage">
                <div className="header-buttons-container">
                    <button className="homepage-button" onClick={urlTravel.execute("/inicio/iniciar_sesion")}>Iniciar sesion</button>
                    <button className="homepage-button" onClick={urlTravel.execute("/inicio/acerca_de_VDV")}>Acerca de VDV</button>
                    <button className="homepage-button" /*Enviar a pagina de reportes*/>Solicitar acceso</button>
                </div>
            </header>
            <div className="form-container">
                <form className="form-style">
                    <h4 className="text-header">Visualizador dinamico de ventas</h4>
                    <input className="input-style"
                    type="text"
                    id="username"
                    placeholder="Usuario KOF:"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                >
                    </input>
                    <input className= "input-style"
                    type="password"
                    id="password"
                    placeholder="Clave:"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    />
                    <button className="login-button" onClick={handleSubmit}>Ingresar</button>               
                    {errorMessage && <p className="error-message">{errorMessage}</p>} 
                    <p>Problemas de acceso? <a href="https://www.google.com">Pulsa aqui</a></p>
                </form>
            </div>
        </div>
    );



}