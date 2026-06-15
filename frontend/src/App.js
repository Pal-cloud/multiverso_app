import React, { useState } from 'react';
import {
  Box, Container, Typography, TextField, Select, MenuItem,
  FormControl, InputLabel, Button, CircularProgress, Paper,
  Chip, Grid, Divider, Fade
} from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import AutoAwesomeIcon from '@mui/icons-material/AutoAwesome';
import DownloadIcon from '@mui/icons-material/Download';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import Swal from 'sweetalert2';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || '';

// ── Tema oscuro personalizado ─────────────────────────────────────────────────
const theme = createTheme({
  palette: {
    mode: 'dark',
    primary:   { main: '#a78bfa' },
    secondary: { main: '#60a5fa' },
    background: { default: '#0f0f1a', paper: 'rgba(255,255,255,0.05)' },
    text: { primary: '#f1f5f9', secondary: '#94a3b8' },
  },
  typography: {
    fontFamily: "'Inter', sans-serif",
    h3: { fontWeight: 700 },
  },
  components: {
    MuiPaper: {
      styleOverrides: {
        root: {
          backdropFilter: 'blur(10px)',
          border: '1px solid rgba(167,139,250,0.2)',
          borderRadius: 16,
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 10,
          textTransform: 'none',
          fontWeight: 600,
          fontSize: '1rem',
          padding: '12px 28px',
        },
      },
    },
    MuiOutlinedInput: {
      styleOverrides: {
        root: {
          borderRadius: 10,
          '& fieldset': { borderColor: 'rgba(167,139,250,0.3)' },
          '&:hover fieldset': { borderColor: '#a78bfa' },
        },
      },
    },
  },
});

const PLATAFORMAS = ['Blog', 'Twitter/X', 'Instagram', 'LinkedIn'];
const MODELOS     = ['Llama 3.3 70B', 'Llama 3.1 8B', 'Gemma 2 9B'];
const IDIOMAS     = ['Español', 'English', 'Français', 'Italiano'];

const TONO_SUGERIDO = {
  'Blog':       'informativo y cercano',
  'Twitter/X':  'directo y conversacional',
  'Instagram':  'visual, inspirador y emocional',
  'LinkedIn':   'profesional y reflexivo',
};

// ── Componente principal ──────────────────────────────────────────────────────
export default function App() {
  const [form, setForm] = useState({
    plataforma: 'Blog',
    modelo:     'Llama 3.3 70B',
    audiencia:  '',
    idioma:     'Español',
    tono:       TONO_SUGERIDO['Blog'],
    tema:       '',
  });
  const [resultado, setResultado] = useState('');
  const [cargando,  setCargando]  = useState(false);

  const handleChange = (field) => (e) => {
    const value = e.target.value;
    setForm((prev) => ({
      ...prev,
      [field]: value,
      ...(field === 'plataforma' ? { tono: TONO_SUGERIDO[value] } : {}),
    }));
  };

  const handleGenerar = async () => {
    if (!form.tema.trim()) {
      Swal.fire({ icon: 'warning', title: 'Tema requerido',
        text: 'Por favor introduce un tema antes de generar.',
        background: '#1a1a2e', color: '#f1f5f9', confirmButtonColor: '#a78bfa' });
      return;
    }
    if (!form.audiencia.trim()) {
      Swal.fire({ icon: 'warning', title: 'Audiencia requerida',
        text: 'Por favor especifica la audiencia objetivo.',
        background: '#1a1a2e', color: '#f1f5f9', confirmButtonColor: '#a78bfa' });
      return;
    }
    setCargando(true);
    setResultado('');
    try {
      const { data } = await axios.post(`${API_URL}/generar`, form);
      setResultado(data.contenido);
      Swal.fire({ icon: 'success', title: '¡Contenido listo!',
        toast: true, position: 'top-end', showConfirmButton: false,
        timer: 2500, background: '#1a1a2e', color: '#f1f5f9' });
    } catch (err) {
      Swal.fire({ icon: 'error', title: 'Error al generar',
        text: err.response?.data?.detail || 'Error inesperado.',
        background: '#1a1a2e', color: '#f1f5f9', confirmButtonColor: '#a78bfa' });
    } finally {
      setCargando(false);
    }
  };

  const handleCopiar = () => {
    navigator.clipboard.writeText(resultado);
    Swal.fire({ icon: 'success', title: 'Copiado al portapapeles',
      toast: true, position: 'top-end', showConfirmButton: false,
      timer: 1800, background: '#1a1a2e', color: '#f1f5f9' });
  };

  const handleDescargar = () => {
    const blob = new Blob([resultado], { type: 'text/plain' });
    const url  = URL.createObjectURL(blob);
    const a    = document.createElement('a');
    a.href     = url;
    a.download = `multiverso_${form.plataforma.toLowerCase().replace('/', '_')}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  // ── Render ──────────────────────────────────────────────────────────────────
  return (
    <ThemeProvider theme={theme}>
      <Box sx={{
        minHeight: '100vh',
        background: 'linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%)',
        py: 6,
      }}>
        <Container maxWidth="md">

          {/* Cabecera */}
          <Box textAlign="center" mb={5}>
            <Typography variant="h3" sx={{
              background: 'linear-gradient(90deg, #a78bfa, #60a5fa, #34d399)',
              WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent',
              mb: 1,
            }}>
              🌐 MultiversoApp
            </Typography>
            <Typography variant="body1" color="text.secondary">
              Genera contenido listo para publicar — impulsado por Groq + LangChain
            </Typography>
          </Box>

          {/* Formulario */}
          <Paper elevation={0} sx={{ p: 4, mb: 4 }}>
            <Grid container spacing={3}>

              <Grid item xs={12} sm={6}>
                <FormControl fullWidth>
                  <InputLabel>Plataforma</InputLabel>
                  <Select value={form.plataforma} label="Plataforma" onChange={handleChange('plataforma')}>
                    {PLATAFORMAS.map((p) => <MenuItem key={p} value={p}>{p}</MenuItem>)}
                  </Select>
                </FormControl>
              </Grid>

              <Grid item xs={12} sm={6}>
                <FormControl fullWidth>
                  <InputLabel>Modelo de IA</InputLabel>
                  <Select value={form.modelo} label="Modelo de IA" onChange={handleChange('modelo')}>
                    {MODELOS.map((m) => <MenuItem key={m} value={m}>{m}</MenuItem>)}
                  </Select>
                </FormControl>
              </Grid>

              <Grid item xs={12} sm={6}>
                <TextField fullWidth label="Audiencia objetivo"
                  placeholder="Ej: jóvenes emprendedores, padres, estudiantes…"
                  value={form.audiencia} onChange={handleChange('audiencia')} />
              </Grid>

              <Grid item xs={12} sm={6}>
                <FormControl fullWidth>
                  <InputLabel>Idioma</InputLabel>
                  <Select value={form.idioma} label="Idioma" onChange={handleChange('idioma')}>
                    {IDIOMAS.map((i) => <MenuItem key={i} value={i}>{i}</MenuItem>)}
                  </Select>
                </FormControl>
              </Grid>

              <Grid item xs={12}>
                <TextField fullWidth label="Tono" value={form.tono}
                  onChange={handleChange('tono')}
                  helperText="Sugerido automáticamente según la plataforma, editable" />
              </Grid>

              <Grid item xs={12}>
                <TextField fullWidth multiline rows={4} label="Tema / Idea"
                  placeholder="Describe sobre qué quieres escribir…"
                  value={form.tema} onChange={handleChange('tema')} />
              </Grid>

              <Grid item xs={12}>
                <Button fullWidth variant="contained" size="large"
                  onClick={handleGenerar} disabled={cargando}
                  startIcon={cargando ? <CircularProgress size={20} color="inherit" /> : <AutoAwesomeIcon />}
                  sx={{ background: 'linear-gradient(90deg, #7c3aed, #2563eb)',
                    '&:hover': { opacity: 0.88 } }}>
                  {cargando ? 'Generando contenido…' : 'Generar contenido'}
                </Button>
              </Grid>

            </Grid>
          </Paper>

          {/* Resultado */}
          <Fade in={!!resultado}>
            <Box>
              {resultado && (
                <Paper elevation={0} sx={{ p: 4 }}>
                  <Box display="flex" justifyContent="space-between" alignItems="center" mb={2}>
                    <Typography variant="h6" color="primary">
                      Contenido para {form.plataforma}
                    </Typography>
                    <Box display="flex" gap={1}>
                      <Chip icon={<ContentCopyIcon />} label="Copiar"
                        onClick={handleCopiar} clickable variant="outlined"
                        sx={{ borderColor: '#a78bfa', color: '#a78bfa' }} />
                      <Chip icon={<DownloadIcon />} label="Descargar .txt"
                        onClick={handleDescargar} clickable variant="outlined"
                        sx={{ borderColor: '#60a5fa', color: '#60a5fa' }} />
                    </Box>
                  </Box>
                  <Divider sx={{ mb: 2, borderColor: 'rgba(167,139,250,0.2)' }} />
                  <Typography variant="body1" sx={{ whiteSpace: 'pre-wrap', lineHeight: 1.8 }}>
                    {resultado}
                  </Typography>
                </Paper>
              )}
            </Box>
          </Fade>

        </Container>
      </Box>
    </ThemeProvider>
  );
}
