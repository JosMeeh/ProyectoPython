import React, { useEffect, useState } from 'react';
import './App.css'



//Ejemplo de uso de axio para la autenticacion

const GoogleBooksSearch: React.FC = () => {
    const [statusCode, setStatusCode] = useState<number | null>(null);

    useEffect(() => {
        const postData = async () => {
            try {
                // Realiza una solicitud POST (esto es solo para el ejemplo)
                const response = await axios.post('https://localhost:7058/Authentication', {
                    userName: "tveestjnunez",
                    password: "Cocacolafemsa.2024#1"
                });
                setStatusCode(response.status);
            } catch (error) {
                if (axios.isAxiosError(error) && error.response) {
                    setStatusCode(error.response.status);
                } else {
                    setStatusCode(500); // Código de error genérico
                }
            }
        };
        postData();
    }, []);

    return (
        <div>
            {statusCode !== null ? (
                <p>Codigo de estado: {statusCode}</p>
            ) : (
                <p>Cargando...</p>
            )}
        </div>
    );
};

export default GoogleBooksSearch;