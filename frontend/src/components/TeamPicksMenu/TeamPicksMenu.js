import * as React from 'react';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import { ImageListItemBar, Typography } from '@mui/material';
import Card from '@mui/material/Card';
import CardActionArea from '@mui/material/CardActionArea';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
function TeamPicksMenu() {

    return (
        //<div>Scrollable List</div>
        <CardActionArea component='a' href='#'>
            <Card sx={{display: 'flex'}}>
                <CardContent sx={{flex:1}}>
                    <Typography component="h2" variant="h5">
                        {"Pick 1:"}
                    </Typography>
                    <Typography variant="subtitle1" paragraph>
                        {"Test Desc"}
                    </Typography>
                </CardContent>
            </Card>
        </CardActionArea>
    );
}

export default TeamPicksMenu;