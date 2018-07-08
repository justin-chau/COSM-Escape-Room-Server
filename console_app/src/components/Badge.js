import React from "react";
import Icon from "../1x/Asset 2.png"

class Badge extends React.Component {
    render() {
        return (
            <div className='helios_badge'>
                <img src={Icon} alt=""/>
                <div className='text_badge'>
                    <p className='title'>HELIOS REPUBLIC</p>
                    <p>CBT-1855 CONTROL SYSTEM</p>
                </div>
            </div>
        );
    }
};

export default Badge;