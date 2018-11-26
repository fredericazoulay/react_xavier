import React from 'react';
import logo from './logo.png';
import './Header.css';
import { Link } from 'react-router-dom';

const Header = () => {
    return (
        <div className="header">
            <Link to="/">
                <img src={logo} alt="logo" className="header__logo" />
            </Link>


                <nav class="header__nav">
                    <ul class="header__list">
                        
                            <li class="header__list-item" data-url="story/">
                                <a target="_self" href="/story/">Our Story</a>
                            </li>
                        
                            <li class="header__list-item" data-url="expertise/">
                                <a target="_self" href="/expertise/">Expertise</a>
                            </li>
                        
                            <li class="header__list-item" data-url="network/">
                                <a target="_self" href="/network/">Network</a>
                            </li>
                        
                            <li class="header__list-item" data-url="news/">
                                <a target="_self" href="/news/">News</a>
                            </li>
                        
                            <li class="header__list-item" data-url="offices/">
                                <a target="_self" href="/offices/">Contact</a>
                            </li>
                        
                    </ul>
                </nav>


        </div>
    );
}

export default Header;