import React from "react";

class Log extends React.Component {
    render() {
        return (
            <div className='helios_log'>
                <div>
                    <p>> HELIOS REPUBLIC CBT-1855 CONTROL SYSTEM</p>
                    <p>> BOOT SEQUENCE COMPLETE</p>
                    <p>> DOOR STATUS: UNLOCKED</p>
                    <p>> ENTER ENCRYPTION KEY</p>
                </div>
                <form>
                    <input type="text" placeholder="Enter ship door encryption key..."/>
                    <button>AUTHENTICATE</button>
                </form>
                <div className='helios_colors'>
                    <div className='helios_red'></div>
                    <div className='helios_blue'></div>
                    <div className='helios_green'></div>
                </div>
            </div>
        );
    }
};

export default Log;