export default (posts = [], action) => {
    switch (action.type) {
        case 'FETCHALL': 
            return posts;
        case 'CREATE':
            return posts;
        default:
            return posts;
    }
}