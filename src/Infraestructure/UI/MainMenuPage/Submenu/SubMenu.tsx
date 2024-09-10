import React from 'react';
import "./SubMenu.css";
interface SubmenuOption {
    label: string;
    onClick: () => void;
}

interface SubmenuProps {
    options: SubmenuOption[];
}

const Submenu: React.FC<SubmenuProps> = ({ options }) => {
    return (
        <div className="submenu-container">
            <div className="submenu">
                {options.map((option, index) => (
                    <button key={index} onClick={option.onClick}>
                        {option.label}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default Submenu;