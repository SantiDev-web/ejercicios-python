import React, { useState } from "react";
import { Box, TextField, Button, Typography, Paper } from "@mui/material";
import { styled } from '@mui/system';
import '@fontsource/inter';

const FormContainer = styled(Paper)(({ theme }) => ({
    padding: theme.spacing(4),
    maxWidth: 400,
    backgroundColor: 'rgba(255, 255, 255, 0)', // Fondo transparente
    borderRadius: 10,
    border: '2px solid white', // Líneas marcadas en negro
    margin: '200px',
    boxShadow: '10px 10px 20px rgba(0, 0, 0, 0.5)', // Sombra para efecto 3D
}));

const CustomTextField = styled(TextField)(() => ({
    '& .MuiInputBase-input': {
        backgroundColor: 'rgba(255, 255, 255, 0)', // Fondo transparente para el input
        color: 'white', // Color del texto del input
        '&:-webkit-autofill': {
            WebkitBoxShadow: '0 0 0 1000px rgba(255, 255, 255, 0) inset', // Fondo transparente para el autocompletado
            WebkitTextFillColor: 'white', // Color del texto para el autocompletado
        },
    },
    '& .MuiOutlinedInput-root': {
        '& fieldset': {
            borderColor: 'white', // Color del borde
        },
        '&:hover fieldset': {
            borderColor: 'white', // Color del borde al pasar el ratón
        },
        '&.Mui-focused fieldset': {
            borderColor: 'white', // Color del borde al estar enfocado
        },
    },
}));

const Login: React.FC = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        // Aquí puedes manejar la lógica de envío del formulario
        console.log({ email, password });
    };

    return (
        <FormContainer elevation={3}>
            <Typography variant="h4" component="h1" gutterBottom sx={{color:'white', textAlign:'center'}}>
                Iniciar Sesion
            </Typography>
            <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                <CustomTextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="email"
                    label="Email Address"
                    name="email"
                    autoComplete="email"
                    autoFocus
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <CustomTextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    name="password"
                    label="Password"
                    type="password"
                    id="password"
                    autoComplete="current-password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    sx={{
                        mt: 3,
                        mb: 2,
                        backgroundColor: 'black',
                        color: 'white',
                        '&:hover': {
                            backgroundColor: 'rgba(0, 0, 0, 0.8)', // Fondo ligeramente más claro al pasar el ratón
                        },
                        '&:focus': {
                            backgroundColor: 'black', // Mantener el mismo fondo al hacer clic
                        },
                    }}
                >
                    Sign In
                </Button>
            </Box>
        </FormContainer>
    );
};

export default Login;
