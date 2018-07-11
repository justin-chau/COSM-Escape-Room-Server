import React from "react";

class Log extends React.Component {
    render() {
        return (
            <div className='helios_log'>
                <div>
                    <p>> HELIOS REPUBLIC CBT-1855 CONTROL SYSTEM</p>
                    <p>> -------------- </p>
                    <p>> BOOT SEQUENCE COMPLETE</p>
                    { this.props.code_verified ? <p className='log_success'>> DOOR STATUS: LOCKED</p> : <p className='log_warning'>> DOOR STATUS: UNLOCKED</p> }
                    <p>> ENTER ENCRYPTION KEY</p>
                    { this.props.current_code ? this.props.code_verified ? <p className='log_success'>> AUTHENTICATED </p> : <p className='log_warning'>> ENCRYPTION KEY REJECTED </p> : null}
                    { this.props.code_verified ? <p>> ENTER DESTINATION COORDINATES </p> : null }
                    { this.props.current_coordinates ? this.props.coordinates_verified ? <p className='log_success'>> COORDINATES ACCEPTED - SETTING TARGET </p> : <p  className='log_warning'>> COORDINATES REJECTED </p> : null }
                    { this.props.coordinates_verified ? <p className='log_warning'>> LOW POWER DETECTED - ENGINE STARTUP FAILURE </p> : null }
                </div>
                <form onSubmit = { this.props.code_verified ? this.props.sendCoordinates : this.props.sendCode }>
                    { this.props.code_verified ? <input type="text" autoComplete="off" placeholder="Enter coordinates..." name="coordinate_field"/> : 
                    <input type="text" autoComplete="off" placeholder="Enter ship door encryption key..." name="code_field"/> }
                    <button>{ this.props.code_verified ? 'ENTER' : 'AUTHENTICATE' }</button>
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