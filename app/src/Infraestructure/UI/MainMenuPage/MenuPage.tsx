import React, { useEffect, useState } from 'react';
import "../MainMenuPage/MenuPage.css";
import FilterMenu from "../FilterMenu/FilterMenu";

export default function MenuPage () {
    const [showFilterMenu, setShowFilterMenu] = useState(false); // New state for FilterMenu visibility

    const handleFilterMenuClick = (option: any) => {
        if (option === 'consultas') {
            setShowFilterMenu(true); // Muestra el FilterMenu solo si se selecciona "Consultas"
        } else {
            setShowFilterMenu(false); // Oculta el FilterMenu al seleccionar cualquier otra opción
        }
    };

   
   
    useEffect(() => {
    const btn = document.getElementById("btn");
    const sidebar = document.getElementsByClassName("Sidebar")[0]; 

    if (btn && sidebar) {
      btn.onclick = function () {
        sidebar.classList.toggle("active");
      }
    }
  }, []); 

  return (
      <div>
        <div className="Sidebar">
          <div className="Logo_content">
            <div className="Logo">
              <i className='bx bx-bar-chart-alt'></i>
              <div className="Logo_name">Visualizador dinamico</div>
            </div>
            <i className='bx bx-menu' id="btn"></i>
            <ul className="nav_list">
              <li>
                  <a href="#" onClick={() => handleFilterMenuClick('inicio')}>
                  <i className='bx bxs-grid-alt bx-flip-vertical'></i>
                  <span className="links_name">Inicio </span>
                </a>
                <span className="tooltip">Inicio </span>
              </li>
              <li>
                  <a href="#" onClick={() => handleFilterMenuClick('consultas')}>
                  <i className='bx bx-package'></i>
                  <span className="links_name">Consultas</span>
                </a>
                <span className="tooltip">Consultas </span>
              </li>
              <li>
                  <a href="#" onClick={() => handleFilterMenuClick('reportes')}>
                  <i className='bx bxs-report'></i>
                  <span className="links_name">Reportes </span>
                </a>
                <span className="tooltip">Reportes </span>
              </li>
              <li>
                  <a href="#" onClick={() => handleFilterMenuClick('configuracion')}>
                  <i className='bx bxs-cog'></i>
                  <span className="links_name">Configuracion </span>
                </a>
                <span className="tooltip">Configuracion </span>
              </li>
              <li>
                <a href="#"> {/*Los onclick aqui*/}
                  <i className='bx bxs-log-out' id="log_out"></i>
                  <span  className="links_name">Salir </span>
                </a>
                <span className="tooltip">Salir </span>
              </li>
            </ul>
              </div>
        </div>
        <div className="Home_content">
              {showFilterMenu && <FilterMenu />} {/* Conditionally render FilterMenu */}            
        </div>
      </div>
  );
};

