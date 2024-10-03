import { JsonData } from "../Dtos/Types/JsonDataType";
export class apiRoutes{

    async getClients(): Promise<any> {
        try {
            const response = await axios.get('https://localhost:7058/clients', {            
            });;
            if (response) {
                console.log(response.status)
                return response;
            } else return null;
        } catch (error) {
            if (axios.isAxiosError(error) && error.response) {
                return error.response; 
            } else {               
                return null; 
            }
        }

    }

    async authentication(username: string, password: string): Promise<any> {
        try {
            const response = await axios.post('https://localhost:7058/Authentication', {
                userName: username,
                password: password 
            });
            if (response) {
                console.log(response.status)
                return response;
            } else return null;
        } catch (error) {
            if (axios.isAxiosError(error) && error.response) {
                return error.response; 
            } else {               
                return null; 
            }
        }
    }
    async dynamicConsult(): Promise<any> {         
            try {
                const response = await axios.post<JsonData>("https://localhost:7058/Data", {                
                        Filters: [
                            {
                                colunm_select: [
                                    ""
                                ],
                                table_name: "Tabla_Clientes",  //TENEMOS QUE CONSTRUIR EL JSON DINAMICAMENTE, SO, ESTO ES UNA PRUEBA
                                filter_values: [
                                    {
                                        column_name: "Localidad",
                                        value: "30 LOS CORTIJOS",
                                        operator: "Equal"
                                    },                              
                                ]
                        },                      
                        ]                   
                });                               
                return response;
            } catch (error) {
                if (axios.isAxiosError(error) && error.response) {
                    return error.response;z
                } else {
                    return null;
                }
            }
        return null;
    }
    static get(): apiRoutes {
        return new apiRoutes();
    }
}