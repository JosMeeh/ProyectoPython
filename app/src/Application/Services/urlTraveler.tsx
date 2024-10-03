import { MouseEventHandler } from "react";
import { IServices } from "../Interfaces/IServices";

export class urlTraveler implements IServices<string, MouseEventHandler<HTMLButtonElement>> {
    
     execute(url: string):() => void { //<button onClick={urlTraveler("/Calamardo")}>Ir a Home</button> INVOCACION CON BOTON O LO QUE SEA
     return () => {
        window.location.href = url;
        };
    };

    static get(): IServices<string, MouseEventHandler<HTMLButtonElement>> {
        return new urlTraveler();
    }
}




