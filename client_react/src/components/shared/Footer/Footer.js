import React from 'react';
//import logo from './logo.png';
import './Footer.css';
//import { Link } from 'react-router-dom';

const Footer = () => {
    return (

<div className="footer">
<footer class="footer">
                <div class="footer__content">
                    <span class="footer__copy">
                        © 2018 ENDEAVOR, LLC. ALL RIGHTS RESERVED. IMG IS AN ENDEAVOR COMPANY.
                    </span>

                    <ul class="footer__list">
                        
                            <li class="footer__list-item">
                                <a target="_self" href="/careers/">Careers</a>
                            </li>
                        
                            <li class="footer__list-item">
                                <a target="_self" href="/tos/">Terms of Use</a>
                            </li>
                        
                            <li class="footer__list-item">
                                <a target="_self" href="/privacypolicy/">Privacy Policy</a>
                            </li>
                        
                            <li class="footer__list-item">
                                <a target="_self" href="/cookiepolicy/">Cookie Policy</a>
                            </li>
                        
                    </ul>
                </div>
                </footer>
    </div>

            );
            }

export default Footer;