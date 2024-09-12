import React, { useEffect } from 'react';
import "./App.css";
const App = () => {
  const handleClick = () => {
    console.log("Se hizo clic en Salir");
  };
  useEffect(() => {
    const btn = document.getElementById("btn"); // Sin el #
    const sidebar = document.getElementsByClassName("Sidebar")[0]; // Sin el . y usando [0]

    if (btn && sidebar) {
      btn.onclick = function () {
        sidebar.classList.toggle("active");
      }
    }
  }, []); // El array vacío asegura que esto se ejecute una vez al montar el componente

  return (
      <div>
        <div className="Sidebar">
          <div className="Logo_content">
            <div className="Logo">
              <i className='bx bx-bar-chart-alt'></i>
              <div className="Logo_name">VDV</div>
            </div>
            <i className='bx bx-menu' id="btn"></i>
            <ul className="nav_list">
              <li>
                <i className='bx bx-search bx-rotate-90'></i>
                <input type="text" placeholder="Search" />
                <span className="tooltip">Tooltip </span>
              </li>
              <li>
                <a href="#">
                  <i className='bx bxs-grid-alt bx-flip-vertical'></i>
                  <span className="links_name">Inicio </span>
                </a>
                <span className="tooltip">Inicio </span>
              </li>
              <li>
                <a href="#">
                  <i className='bx bx-package'></i>
                  <span className="links_name">Consultas</span>
                </a>
                <span className="tooltip">Consultas </span>
              </li>
              <li>
                <a href="#">
                  <i className='bx bxs-report'></i>
                  <span className="links_name">Reportes </span>
                </a>
                <span className="tooltip">Reportes </span>
              </li>
              <li>
                <a href="#">
                  <i className='bx bxs-cog'></i>
                  <span className="links_name">Configuracion </span>
                </a>
                <span className="tooltip">Configuracion </span>
              </li>
              <li>
                <a href="Salida"> {/*Los onclick aqui*/}
                  <i className='bx bxs-log-out' id="log_out"></i>
                  <span  className="links_name">Salir </span>
                </a>
                <span className="tooltip">Salir </span>
              </li>
            </ul>
          </div>
        </div>
        <div className="Home_content">
          <div className="text">Home Content</div>
        </div>
      </div>
  );
};

export default App;