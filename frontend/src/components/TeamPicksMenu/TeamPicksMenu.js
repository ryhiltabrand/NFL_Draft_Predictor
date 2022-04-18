import * as React from 'react';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import { ImageListItemBar, Typography } from '@mui/material';
import Card from '@mui/material/Card';
import CardActionArea from '@mui/material/CardActionArea';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';

function TeamPick(teamName, pickNumber) {

    return (
        <CardActionArea component='a' href='#'>
            <Card sx={{display: 'flex'}}>
                <CardContent sx={{flex:1}}>
                    <Typography component="h2" variant="h5">
                        {`Pick ${pickNumber}:`}
                    </Typography>
                    <Typography variant="subtitle1" paragraph>
                        {teamName}
                    </Typography>
                </CardContent>
            </Card>
        </CardActionArea>
    )
}

function TeamPicksMenu() {

    var teams = ["Jags", "Lions", "Seahawks", "Bills"];

    var teamPicks = teams.map((teamName, pickNumber) =>
        <div style={{ display: "inline-block" }}>
            {TeamPick(teamName, pickNumber)}
        </div>
    );

    console.log(teamPicks)

    return (
        //<div>Scrollable List</div>
        <div>
            {teamPicks}
        </div>
    );
}

export default TeamPicksMenu;