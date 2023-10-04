import React, { useState, useEffect } from 'react';

function Home(){

    const headerStyle={
        backgroundColor:"red",
        height:"150px"

    }

    const logoStyle={
        color:"white",
        fontSize: '30pt'
    }

    return(
        <div className='container-fluid' style={headerStyle}>
            <h3 style={logoStyle}>Pizza Place</h3>
        </div>
    )
}

export default Home