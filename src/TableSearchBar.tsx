
import {Users} from "./Users.js";
import {useState} from "react";
import dataTable from "./DataTable";
import DataTable from "./DataTable";


export default function Search(){
const [query, setQuery] = useState("");
    const search = (data:any)=>{
    return (data.filter((item:any)=>item.Name.toLowerCase().includes(query)))
    }

    return(
        <div className="table">
            <input type={"text"} placeholder={"Search..."} className={"search"} onChange={(e) => setQuery(e.target.value)}/>
            <DataTable data={search(Users)}/>

        </div>
    );
}