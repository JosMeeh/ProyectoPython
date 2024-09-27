export class AuthUserResponse {

    private username:string;
    private email: string;
    

    constructor(_username: string, _email: string) {
        this.username = _username;
        this.email = _email;
        
    }

    get Getusername(): string {
        return this.username;
    }

    set Setusername(_username: string) {
        this.username = _username;
    }

    get Getemail(): string {
        return this.email;
    }

    set Setemail(_email: string) {
        this.email = _email;
    }

}