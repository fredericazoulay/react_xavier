import React from 'react';
import { handleResponse } from '../../helpers';
import { API_URL } from '../../config';
import TableEtudiants from './TableEtudiants/TableEtudiants.js';
import Loading from '../shared/Loading/Loading';


// Access to fetch at 'http://127.0.0.1:5000/api/v1.0/etudiant' from origin 'http://localhost:3000' has been blocked 
// by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.

class Etudiants extends React.Component {
    constructor() 
    {
        super();
        this.refreshStudent = this.refreshStudent.bind(this);

        this.state = {
            loading: false,
            etudiants: [],
            error: null
        }
    }

    componentDidMount() {
        this.fetchEtudiants();
    }

    //componentDidUpdate() {
        //this.fetchEtudiants();
    //}

    fetchEtudiants() {
        this.setState({ loading: true });
        fetch(`${API_URL}/etudiant`, 
                {
                method: 'get',
                headers: {'Accept': 'application/json', 'Content-Type': 'application/json','Access-Control-Allow-Origin':'GET POST PUT DELETE OPTIONS', 'Access-Control-Allow-Credentials': 'true'}
                }
            )
            .then(handleResponse)
            .then((data) => {
                const etudiants  = data.item;
                console.log(etudiants);
                this.setState({
                    etudiants,
                    loading: false
                });
            })
            .catch((error) => {
                this.setState({ error : error.errorMessage, loading: false });
            });
    }

    refreshStudent(students, student) {
        //getstate();
        console.log('refresh' + student.id_etudiant)
        console.log(students)
        students.splice(students.indexOf(student), 1)
        console.log(students)
        const etudiants  = students;
        console.log(this.props.location.pathname)
        this.setState({
            etudiants
        })
        //console.log(this.state.etudiants.indexOf(student.id_etudiant))
        //this.state.etudiants.splice(this.state.etudiants.indexOf(student.id_etudiant), 1)
    }

    render() {
        const {loading, error, etudiants} = this.state;
        if(loading) {
            return <div className="loading-container"><Loading /></div>
        }
        if(error) {
            return <div className="error">{error}</div>
        }
        return (
            <div>
                <TableEtudiants etudiants={etudiants} rerender={this.refreshStudent}/>
            </div>
        )
    }
}

export default Etudiants;

// <TableEtudiants etudiants={etudiants} rerender={this.fetchEtudiants}/>