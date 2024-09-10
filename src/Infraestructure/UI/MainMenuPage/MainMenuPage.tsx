import "./MainMenuPage.css";
import "../Components/sharedStyles.css";
import Submenu from "./Submenu/SubMenu";
import { useState } from 'react';
import { buildDatatable } from "../../../Application/Services/buildDatatable";
import DataTable from "../MainMenuPage/Datatable/DataTable"; // Asegúrate de que la ruta sea correcta

export default function MainMenuPage() {
    const [activeSubmenu, setActiveSubmenu] = useState<string | null>(null);
    const [dataTableData, setDataTableData] = useState<{ columns: any[]; data: any[] } | null>(null);
    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);
    const databuild: buildDatatable = buildDatatable.get();

    const toggleSubmenu = (submenuId: string) => {
        setActiveSubmenu(activeSubmenu === submenuId ? null : submenuId);
    };

    const handleOptionClick = async (parameters: string) => {
        setLoading(true);
        setError(null); // Reset error state
        try {
            const result = await databuild.execute(parameters);
            if (result) {
                setDataTableData(result);
            } else {
                setError('No data available');
            }
        } catch (err) {
            console.error('Error executing data build:', err);
            setError('Error loading data');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="full-mainmenu">
            <div className="sidebar-menu">
                <div className="sidebar-content-container">
                    <h1>Menu principal</h1>
                    <button>Inicio</button>
                    <button onClick={() => toggleSubmenu('submenuConsultas')}>
                        Consultas
                    </button>
                    {activeSubmenu === 'submenuConsultas' && (
                        <Submenu
                            options={[
                                { label: 'Opción 1', onClick: () => handleOptionClick("pepe") },
                                { label: 'Opción 2', onClick: () => console.log('Consulta Opción 2') },
                            ]}
                        />
                    )}
                    <button onClick={() => toggleSubmenu('submenuReportes')}>
                        Reportes
                    </button>
                    {activeSubmenu === 'submenuReportes' && (
                        <Submenu
                            options={[
                                { label: 'Opción 1', onClick: () => console.log('Reporte Opción 1') },
                                { label: 'Opción 2', onClick: () => console.log('Reporte Opción 2') },
                            ]}
                        />
                    )}
                    <button className="sidebar-sidebar-menu-button-exit">Salir</button>
                </div>
            </div>

            <div className="data-table-wrapper">
                {/* Renderiza el DataTable si hay datos disponibles */}
                {loading && <div>Cargando datos...</div>}
                {error && <div>{error}</div>}
                {dataTableData && (
                    <DataTable columns={dataTableData.columns} data={dataTableData.data} />
                )}
            </div>
        </div>
    );
}