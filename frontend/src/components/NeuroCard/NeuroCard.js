import React from 'react'


const NeuroCard = ({backgroundColor, width, height, borderRadius, children}) => {

    
    const style = {
        container: {
            backgroundColor: backgroundColor,
            width: width,
            height: height,
            borderRadius: borderRadius,

        }
    }

    return(
        <div style={style.container}>
            {children}
        </div>
    )


}



export default NeuroCard