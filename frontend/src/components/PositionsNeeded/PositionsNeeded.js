import axios from "axios"
import { useEffect, useState } from "react";
import Card from "react-bootstrap/Card";

function PositionsNeeded(props) {
    var team = props.team;
    const host = window.location.hostname;
    const port = 8000;

    const [positionsOfNeed, setPositionsOfNeed] = useState([]);
    const [loaded, setLoaded] = useState(false);

    useEffect(() => {
        axios.get(`http://${host}:${port}/pon/${team.acryonm}/`).then((res) => {
            console.log(res.data)
            setPositionsOfNeed(res.data["Positions of Need"])
            setLoaded(true);
        })
    }, []);

    return (
        <div>
        Positions of Need
        {
            loaded ? positionsOfNeed.map((position) =>
                <div>
                    {position}
                </div>
            ) : ""
        }
    </div>
    );
}

export default PositionsNeeded;