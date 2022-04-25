import axios from "axios"
import { useEffect, useState } from "react";


function TeamStats(props) {
    var team = props.team;
    const host = window.location.hostname;
    const port = 8000;

    const [stats, setStats] = useState([]);
    //const [roster, setRoster] = useState([]);
    const [loaded, setLoaded] = useState(false);

    useEffect(() => {
        axios.get(`http://${host}:${port}/data/${team.acryonm}/`).then((res) => {
            setStats(res.data)
            setLoaded(true);
            
        })
    }, []);
    
    return (
        <div>
            Team stats
            {
                loaded ? stats.map((stat) =>
                <div>
                    
                    {console.log(stat)}
                </div>
                ): ""
            } 
            
        </div>
    );
}

export default TeamStats;