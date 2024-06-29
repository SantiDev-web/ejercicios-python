import React from 'react'
import { Box, Typography } from '@mui/material'
import { styled } from '@mui/system'
import { Slide, Fade } from "react-awesome-reveal";
import Stack from '@mui/material/Stack';
import punisherLogo from '../assets/punisher.svg';


const ImgContainer = styled(Box)({
    height: '100vh',
    margin: 0,
    padding: 0,
    background: 'linear-gradient(to top, black, yellow)',
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center'
});

const ContentStack = styled(Stack)({
    position: 'absolute',
    left: '60px',
    top: '50%',
    transform: 'translateY(-50%)',
    textAlign: 'left',
    color: 'white',
    maxWidth: 'calc(100% - 60px)'
  });
const StyledImg = styled('img')({
    width: '200px',
    height: '200px',
    color: 'white',
    filter: 'invert(1)',
    display: 'block',
    margin: '0 auto',
    marginTop:'50px'
  });
const LoginApp: React.FC = () => {
    return (
        <section id='img'>
            <ImgContainer>
                <ContentStack>
                    <Typography variant='h1' component='h1' sx={{ fontFamily: 'Black Ops One', color:'white', textAlign:'center' }}>
                        <Slide delay={2} direction='up'>Fitness Coaching</Slide>
                    </Typography>
                    <Typography variant='h5' component='p' sx={{ fontFamily: 'Black Ops One', color:'white', textAlign:'center' }}>
                    <Fade delay={1e3} cascade damping={1e-1}>ONE MORE REP!!</Fade>
                    </Typography>
                    <StyledImg src={punisherLogo} alt="Punisher Logo" />
                </ContentStack>
            </ImgContainer>
        </section>
    )
};

export default LoginApp;
