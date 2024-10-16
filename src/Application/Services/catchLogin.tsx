import { IServices } from "../Interfaces/IServices";
import { apiRoutes } from "../../Infraestructure/HTTPRoutes/apiRoutes";
import { ResponseBody } from "../../Infraestructure/Dtos/ResponseBody";
import { AuthUserResponse } from "../../Infraestructure/Dtos/AuthUserResponse";
export class catchLogin implements IServices<string[], Promise<ResponseBody<AuthUserResponse>>>{
    apiRoute: apiRoutes = apiRoutes.get();


    async execute(parameter: string[]): Promise<ResponseBody<AuthUserResponse>>{
        const response = await this.apiRoute.authentication(parameter[0], parameter[1]);
        if (response) {
            switch (response.status) {
                case 200:
                    const {data: { userName, email } } = response.data;
                    return new ResponseBody(response.status, "Autenticado", (new AuthUserResponse(userName,email)));
                case 401:
                    return new ResponseBody(response.status, "Contraseña incorrecta", (new AuthUserResponse("", "")));
                case 403:
                    return new ResponseBody(response.status, "No tiene permisos para acceder a la aplicacion", (new AuthUserResponse(userName, email)));
                case 404:
                    return new ResponseBody(response.status, "Usuario no encontrado", (new AuthUserResponse("", "")));
                case 400:
                    return new ResponseBody(response.status, "Un error inesperado ha ocurrido", (new AuthUserResponse("", "")));
            }
        }
        return new ResponseBody(400, "Un error inesperado ha ocurrido", (new AuthUserResponse("", "")));       
    }

     

    static get(): IServices<string[], Promise<ResponseBody<AuthUserResponse>>>{
        return new catchLogin();
    }
}