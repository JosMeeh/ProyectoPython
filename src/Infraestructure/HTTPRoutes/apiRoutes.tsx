import { JsonData } from "../Dtos/Types/JsonDataType";
export class apiRoutes{

    async getData(): Promise<any> {
        try {
            const response = await axios.get('https://localhost:7058/clients');
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
    async dynamicConsult(data: any): Promise<any> {         
        console.log(data)
        try {
                const response = await axios.post<JsonData>("https://localhost:7058/Data", data);                               
                return response;
            } catch (error) {
                if (axios.isAxiosError(error) && error.response) {
                    return error.response;
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