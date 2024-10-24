import { useNavigate } from 'react-router-dom';

const Startpage = () => {
    const navigate = useNavigate();
    navigate('/startpage');
    return (
        <div>
            <h1 style={{ color: '#11557C' }}>Startpage</h1>
        </div>
    );
}

export default Startpage;
