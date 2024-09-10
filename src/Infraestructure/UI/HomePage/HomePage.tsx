
import { urlTraveler } from "../../../Application/Services/urlTraveler";
import "./HomePage.css"
import "../Components/sharedStyles.css"

export default function HomePage() {   
    const service = urlTraveler.get();
    return (
        <div className="full-homepage">
            <div className="flex-container">
                <header className="header-homepage">
                    <div className="header-buttons-container">
                        <button className="homepage-button" onClick={service.execute("/inicio/iniciar_sesion")}>Iniciar sesion</button>
                        <button className="homepage-button" onClick={service.execute("/inicio/acerca_de_VDV")}>Acerca de VDV</button>
                        <button className="homepage-button" /*Enviar a pagina de reportes*/>Solicitar acceso</button>
                    </div>
                </header>
                <main className="main-homepage">
                    <div className="main-buttons-container">
                        <button className="main-button" onClick={service.execute("/inicio/iniciar_sesion")}>Iniciar sesion</button>
                        <button className="main-second-button" onClick={service.execute("/inicio/acerca_de_VDV")}>Acerca de VDV</button>
                        <p>Problemas al acceder a VDV? <a href="https://www.google.com">Pulsa aqui</a> para crear un ticket.</p>
                    </div>
                </main>
            </div> 
            
        </div>       
    );



}