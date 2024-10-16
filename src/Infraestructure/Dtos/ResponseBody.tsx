
export class ResponseBody<T> {

    private response_code: number;
    private response_message: string;
    private data: T

    constructor(_response_code: number, _response_message: string, _data: T) {
        this.response_code = _response_code;
        this.response_message = _response_message;
        this.data = _data;
    }

    get Getresponse_code(): number {
        return this.response_code;
    }

    set Setresponse_code(code: number) {
        this.response_code = code;
    }

    get Getresponse_message(): string {
        return this.response_message;
    }

    set Setresponse_message(message: string) {
        this.response_message = message;
    }

    get Getdata(): T {
        return this.data;
    }

    set Setdata(value: T) {
        this.data = value;
    }

    

}