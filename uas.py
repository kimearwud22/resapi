# import resource
from ast import parse
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

# init app
app = Flask(__name__)
api = Api(app)


# Create Resource Class
# buat class individu
# page home
class Home(Resource):
    def get(self):
        return{
            "header": [
                {
                    "navleft": [
                        {
                            "brand": {
                                "img": "data:image/webp;base64,UklGRmgDAABXRUJQVlA4TFsDAAAvkEAGEPdAmG1UoPPXu+cUBAJJAvvjLhBIAtxfZ4EAYcF/pAQJ/qNYAQMSJElyFKlpMUz3KGC1mv+/86iMqvtBRP8hSJIbt1lJ1hFEHoAASH8hPbfbCdvHe6LtuOiW+3B5eNsUaFWSEmLchWRWkAq4PT85pq4OvJ680cXC3uaFeRwiAGoRlMXXkRVktiCboZXYWOfeHZ3f6kT3HO4+TyDCxALqJB9kMKwzpF+ezi9xYrp42x7lmeHsIAqjj5K9DNtzKNh/rs5XZY56nAMjhjHOXjpnVwM4MgYPWI4ny90egUe7hZsgvDUBj2yO08VgWsY1AaOnAhwt5MOVLT/+EfzKfpM6kMAfToksECBnGzZYXfIS6s7R6owzZHLdn9+jwfqwzr/hIL1iX1hkwEXA01kQ89EFihkLqAHGZWHfJJb2TT/W+YfUFXxDtZCH/dAb4Nli53wMETNereTcLIxJ02sgqGD5p50HlMH77phkCVDs3NOAJATGAjIAHYYZPMoc1Yf0GF+bpKj0dFshwoPbnLhq9zQgsYFxUu0mLIuSgRPwiH3/cOS0XSjHcJvGt5hy8RlnK4nomJUXXgS1yZavfmHN7lFsR/V5Nj6vqsKMQ3Rkk92Vh2KDBlk1936ww6RvC/FCNQOctun7PJnPNYGYcbOy49QPL/VX8izxEuM38WRxc5YS2NACPJXPg7KRGQ9RNhCLN/GmDXp0dyy5N/9IzQQUtyw0SjsGfpNRshq27Gctfwit/kPxGwzcf1DNLPuFq8NvPUkmxsC2E+Mkkrbc3I4nXRCi94Xt+P0kiElrpXH/BZ6FHSkRrcTYraND4kmzfgB8dy1feU6vOvr9AmPrzRv/cYZASR1bFRsfzO21reAM6AbZ+vg8T/1vqINGM7p1XSiqcw5poKVNBXGjW255e+krttTAshlb8wIpqrcjvGwOnCE3tY6thH2m1F9d1hZYNutb0JIcrbH5YYqdxVOwBBVMn5CGu2wWI9OZwRI73hpdNg9xUrO5aKqDJaiDE5sjbiB/sb+6K68JjAPL5gXOIzlqwLgZafpv4A/ImbJu3tWX+VLHEpPziP0U1LMekgsVLWG1ReljnZNhhobqWr7Lj1O2dH7C9ZilnFdAbhIYsAQddpSxne/dcly7JFoCAA==",
                                "url": "https://preview.colorlib.com/theme/dreams/index.html"
                            }
                        },
                        {
                            "navbaritems": [
                                {
                                    "text": "HOME",
                                    "url": "https://preview.colorlib.com/theme/dreams/index.html"
                                },
                                {
                                    "text": "COURSES",
                                    "url": "https://preview.colorlib.com/theme/dreams/courses.html"
                                },
                                {
                                    "text": "HOME",
                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                    "items": [
                                            {
                                                "text": "about",
                                                "url": "https://preview.colorlib.com/theme/dreams/about.html"
                                            },
                                        {
                                                "text": "instructor",
                                                "url": "https://preview.colorlib.com/theme/dreams/instructor.html"
                                                },
                                        {
                                                "text": "Pricing",
                                                "url": "https://preview.colorlib.com/theme/dreams/pricing.html"
                                                },
                                        {
                                                "text": "FAQ",
                                                "url": "https://preview.colorlib.com/theme/dreams/faq.html"
                                                },
                                        {
                                                "text": "Course Detail",
                                                "url": "https://preview.colorlib.com/theme/dreams/course-detail.html"
                                                },
                                        {
                                                "text": "Blog Detail",
                                                "url": "https://preview.colorlib.com/theme/dreams/blog-detail.html"
                                                }
                                    ]
                                },
                                {
                                    "text": "NEWS",
                                    "url": "https://preview.colorlib.com/theme/dreams/blog.html"
                                },
                                {
                                    "text": "CONTACT",
                                    "url": "https://preview.colorlib.com/theme/dreams/contact.html"
                                }
                            ]
                        }
                    ]
                },
                {
                    "navreight": [
                        {
                            "icon": "fa fa-search search-switch",
                            "klik": {
                                    "true": {
                                        "icon": "search-close-switch",
                                        "placeholder": "search here"
                                    }
                            }
                        },
                        {
                            "icon": "fa fa-facebook",
                            "url": "https://preview.colorlib.com/theme/dreams/#"
                        },
                        {
                            "icon": "fa fa-twitter",
                            "url": "https://preview.colorlib.com/theme/dreams/#"
                        },
                        {
                            "icon": "fa fa-instagram",
                            "url": "https://preview.colorlib.com/theme/dreams/#"
                        },
                        {
                            "icon": "fa fa-dribbble",
                            "url": "https://preview.colorlib.com/theme/dreams/#"
                        },
                        {
                            "text": "Get Started",
                            "url": "https://preview.colorlib.com/theme/dreams/#"
                        }
                    ]
                }
            ],
            "body": [
                {
                    "hero_benner": {
                        "bacground_image": "img/hero-bg.jpg",
                        "hero_text": [
                            {
                                "text1": "BEST OPTIONS FOR YOU",
                                "text2": "DRIVE SAFE & GET LICENSE",
                                "hero_text_pilih": [
                                    {
                                        "text": "Contact Us",
                                        "url": "https://preview.colorlib.com/theme/dreams/#"
                                    },
                                    {
                                        "text": "See Courses",
                                        "url": "https://preview.colorlib.com/theme/dreams/#"
                                    }
                                ]
                            }
                        ]
                    },
                    "feature": [
                        {
                            "feactur_text": {
                                "text1": "Why choose us ?",
                                "text2": "Our feature",
                                "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua viverra maecenas facilisis"
                            }
                        },
                        {
                            "feactur_item": [
                                {
                                    "item1": {
                                        "img": "img/feature/xfeature-1.png.pagespeed.ic.22dCgiNvOu.webp",
                                        "text": "Unlimited Car Support"
                                    },
                                    "item2": {
                                        "img": "img/feature/xfeature-2.png.pagespeed.ic.r1evg5EssL.webp",
                                        "text": "Driving School Insures"
                                    },
                                    "item3": {
                                        "img": "img/feature/xfeature-3.png.pagespeed.ic.ZNUFBwu5wI.webp",
                                        "text": "Any Time Any Location"
                                    }
                                }
                            ]
                        }
                    ],
                    "about-vidio": [
                        {
                            "vidio": {
                                "img-bacground-vidio": "img/video-bg.jpg",
                                "button": "btn play-vidio",
                                "url-youtobe": "https://www.youtube.com/watch?v=bGuHgRQSEuk"
                            },
                            "about_vidio_text": [
                                {
                                    "title": {
                                        "text1": "Welcome to Online trafic school",
                                        "text2": "looking for lessons?"
                                    },
                                    "paragraf": {
                                        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum vidnas accumsan lacus velfacilisis.",
                                        "button": {
                                                "text": "Learn more",
                                                "url": "https://preview.colorlib.com/theme/dreams/#"
                                        }
                                    }
                                }
                            ]
                        }
                    ],
                    "application-form": [
                        {
                            "title": {
                                "text1": "Giving Best Option For You",
                                "text2": "Application Form"
                            },
                            "formulir": [
                                {
                                    "input1": {
                                        "placeholder": "Your name"
                                    },
                                    "input2": {
                                        "placeholder": "Your Email"
                                    },
                                    "input3": {
                                        "placeholder": "Your Phone"
                                    },
                                    "input5": {
                                        "placeholder": "Date & time"
                                    },
                                    "option-item1": [
                                        {
                                            "options": {
                                                "option1": "Courses type",
                                                "option2": "Safe Driving Courses",
                                                "option3": "Motorhome Drivers"
                                            },
                                            "list": {
                                                "list1": "Courses type",
                                                "list2": "Safe Driving Courses",
                                                "list3": "Motorhome Drivers"
                                            }
                                        }
                                    ],
                                    "option-item2": [
                                        {
                                            "options": {
                                                "option1": "Car type",
                                                "option2": "Hatcback",
                                                "option3": "Sedan"
                                            },
                                            "list": {
                                                "list1": "Car type",
                                                "list2": "Hatcback",
                                                "list3": "Sedan"
                                            }
                                        }
                                    ],
                                    "button-send": {
                                        "text": "SEND INQUIRY"
                                    }
                                }
                            ]
                        }
                    ],
                    "pricing": [
                        {
                            "pricing-title": {
                                "text1": "Get Spesial Offer",
                                "text2": "Our Pricing"
                            },
                            "pricing-item1": [
                                {
                                    "text-top": "20% off",
                                    "price": "$ 199",
                                    "text": "Personal Driving"
                                },
                                {
                                    "list-item-pricing": {
                                        "list1": "Full course theory",
                                        "list2": "Full driving course",
                                        "list3": "Training in first aid",
                                        "list4": "Practical sessions",
                                        "list5": "Psychological support"
                                    }
                                },
                                {
                                    "text": "GET STARTED",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                }
                            ],
                            "pricing-item2": [
                                {
                                    "text-top": "20% off",
                                    "price": "$ 379",
                                    "text": "Power Booster"
                                },
                                {
                                    "list-item-pricing": {
                                        "list1": "Full course theory",
                                        "list2": "Full driving course",
                                        "list3": "Training in first aid",
                                        "list4": "Practical sessions",
                                        "list5": "Psychological support"
                                    }
                                },
                                {
                                    "text": "GET STARTED",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                }
                            ],
                            "pricing-item3": [
                                {
                                    "text-top": "20% off",
                                    "price": "$ 259",
                                    "text": "Freight Driving"
                                },
                                {
                                    "list-item-pricing": {
                                        "list1": "Full course theory",
                                        "list2": "Full driving course",
                                        "list3": "Training in first aid",
                                        "list4": "Practical sessions",
                                        "list5": "Psychological support"
                                    }
                                },
                                {
                                    "text": "GET STARTED",
                                    "url": "https://preview.colorlib.com/theme/dreams/?#"
                                }
                            ]
                        }
                    ],
                    "team": [
                        {
                            "team-title": {
                                "text1": "Our Great Team",
                                "text2": "Our Instructor",
                                "btn-team-all": {
                                    "text": "View all",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                }
                            },
                            "team-item": [
                                {
                                    "team-item1": [
                                        {
                                            "item-img": {
                                                "img": "img/team/xteam-1.png.pagespeed.ic.cHiltCofrK.webp"
                                            },
                                            "item-text": {
                                                "text1": "DAVID WARNER",
                                                "text2": "Instructor",
                                                "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                            },
                                            "item-social": {
                                                "url": "https://preview.colorlib.com/theme/dreams/#",
                                                "icon": {
                                                    "icon1": "fa fa-fecebook",
                                                    "icon2": "fa fa-twitter",
                                                    "icon3": "fa fa-instagram",
                                                    "icon4": "fa fa-dribbble"
                                                }
                                            }
                                        }
                                    ],
                                    "team-item2": [
                                        {
                                            "item-img": {
                                                "img": "img/team/xteam-2.png.pagespeed.ic.dZB3yfmD0i.webp"
                                            },
                                            "item-text": {
                                                "text1": "DAVID WARNER",
                                                "text2": "Instructor",
                                                "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                            },
                                            "item-social": {
                                                "url": "https://preview.colorlib.com/theme/dreams/#",
                                                "icon": {
                                                    "icon1": "fa fa-fecebook",
                                                    "icon2": "fa fa-twitter",
                                                    "icon3": "fa fa-instagram",
                                                    "icon4": "fa fa-dribbble"
                                                }
                                            }
                                        }
                                    ],
                                    "team-item3": [
                                        {
                                            "item-img": {
                                                "img": "img/team/xteam-3.png.pagespeed.ic.AOhA2y9pBh.webp"
                                            },
                                            "item-text": {
                                                "text1": "DAVID WARNER",
                                                "text2": "Instructor",
                                                "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                            },
                                            "item-social": {
                                                "url": "https://preview.colorlib.com/theme/dreams/#",
                                                "icon": {
                                                    "icon1": "fa fa-fecebook",
                                                    "icon2": "fa fa-twitter",
                                                    "icon3": "fa fa-instagram",
                                                    "icon4": "fa fa-dribbble"
                                                }
                                            }
                                        }
                                    ],
                                    "team-item4": [
                                        {
                                            "item-img": {
                                                "img": "img/team/xteam-4.png.pagespeed.ic.x98B_rqu1y.webp"
                                            },
                                            "item-text": {
                                                "text1": "DAVID WARNER",
                                                "text2": "Instructor",
                                                "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                            },
                                            "item-social": {
                                                "url": "https://preview.colorlib.com/theme/dreams/#",
                                                "icon": {
                                                    "icon1": "fa fa-fecebook",
                                                    "icon2": "fa fa-twitter",
                                                    "icon3": "fa fa-instagram",
                                                    "icon4": "fa fa-dribbble"
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ],
            "footer": [
                {
                    "body-footer": [
                        {
                            "footer-widget1": [
                                {
                                    "title": {
                                        "text": "COMPANY"
                                    }
                                },
                                {
                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                    "list": {
                                        "list1": "About Us",
                                        "list2": "Company",
                                        "list3": "Press & blog",
                                        "list4": "Privacy Policy",
                                        "list5": "Faq"
                                    }
                                }
                            ],
                            "footer-widget2": [
                                {
                                    "title": {
                                        "text": "Courses"
                                    }
                                },
                                {
                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                    "list": {
                                        "list1": "Winter driving",
                                        "list2": "Program for seniors",
                                        "list3": "Adult in car lesons",
                                        "list4": "Defensive driving",
                                        "list5": "Stick shift lessons"
                                    }
                                }
                            ],
                            "footer-widget3": [
                                {
                                    "title": {
                                        "text": "USEFUL LINKS"
                                    }
                                },
                                {
                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                    "list": {
                                        "list1": "Home",
                                        "list2": "Drupal Themes",
                                        "list3": "Wordpress Themes",
                                        "list4": "Support",
                                        "list5": "Services"
                                    }
                                }
                            ],
                            "footer-about": [
                                {
                                    "logo": {
                                        "img": "img/xfooter-logo.png.pagespeed.ic.m_mZ4QWNCF.webp",
                                        "text": "Address : 15 Division Street, New York, NY 12032, United States of America"
                                    }
                                },
                                {
                                    "list": {
                                        "phone": "+0 (123) 456789",
                                        "Email": "kaseo@gmail.com",
                                        "Fax": "+8 (123) 456 789"
                                    }
                                }
                            ]
                        }
                    ],
                    "footer-finis": {
                        "text": "Copyright © 2022 All rights reserved | This template is made with",
                        "icon": "fa fa-heart",
                        "blank": {
                                "text": "Colorlib",
                                "url": "https://colorlib.com/"
                        }
                    }
                }
            ]
        }

# page courses


class Courses(Resource):
    def get(self):
        return {
            "header": [
                {
                    "navleft": [
                        {
                            "brand": {
                                "img": "data:image/webp;base64,UklGRmgDAABXRUJQVlA4TFsDAAAvkEAGEPdAmG1UoPPXu+cUBAJJAvvjLhBIAtxfZ4EAYcF/pAQJ/qNYAQMSJElyFKlpMUz3KGC1mv+/86iMqvtBRP8hSJIbt1lJ1hFEHoAASH8hPbfbCdvHe6LtuOiW+3B5eNsUaFWSEmLchWRWkAq4PT85pq4OvJ680cXC3uaFeRwiAGoRlMXXkRVktiCboZXYWOfeHZ3f6kT3HO4+TyDCxALqJB9kMKwzpF+ezi9xYrp42x7lmeHsIAqjj5K9DNtzKNh/rs5XZY56nAMjhjHOXjpnVwM4MgYPWI4ny90egUe7hZsgvDUBj2yO08VgWsY1AaOnAhwt5MOVLT/+EfzKfpM6kMAfToksECBnGzZYXfIS6s7R6owzZHLdn9+jwfqwzr/hIL1iX1hkwEXA01kQ89EFihkLqAHGZWHfJJb2TT/W+YfUFXxDtZCH/dAb4Nli53wMETNereTcLIxJ02sgqGD5p50HlMH77phkCVDs3NOAJATGAjIAHYYZPMoc1Yf0GF+bpKj0dFshwoPbnLhq9zQgsYFxUu0mLIuSgRPwiH3/cOS0XSjHcJvGt5hy8RlnK4nomJUXXgS1yZavfmHN7lFsR/V5Nj6vqsKMQ3Rkk92Vh2KDBlk1936ww6RvC/FCNQOctun7PJnPNYGYcbOy49QPL/VX8izxEuM38WRxc5YS2NACPJXPg7KRGQ9RNhCLN/GmDXp0dyy5N/9IzQQUtyw0SjsGfpNRshq27Gctfwit/kPxGwzcf1DNLPuFq8NvPUkmxsC2E+Mkkrbc3I4nXRCi94Xt+P0kiElrpXH/BZ6FHSkRrcTYraND4kmzfgB8dy1feU6vOvr9AmPrzRv/cYZASR1bFRsfzO21reAM6AbZ+vg8T/1vqINGM7p1XSiqcw5poKVNBXGjW255e+krttTAshlb8wIpqrcjvGwOnCE3tY6thH2m1F9d1hZYNutb0JIcrbH5YYqdxVOwBBVMn5CGu2wWI9OZwRI73hpdNg9xUrO5aKqDJaiDE5sjbiB/sb+6K68JjAPL5gXOIzlqwLgZafpv4A/ImbJu3tWX+VLHEpPziP0U1LMekgsVLWG1ReljnZNhhobqWr7Lj1O2dH7C9ZilnFdAbhIYsAQddpSxne/dcly7JFoCAA==",
                                "url": "https://preview.colorlib.com/theme/dreams/index.html"
                            }
                        },
                        {
                            "navbaritems": [
                                {
                                    "text": "HOME",
                                    "url": "https://preview.colorlib.com/theme/dreams/index.html"
                                },
                                {
                                    "text": "COURSES",
                                    "url": "https://preview.colorlib.com/theme/dreams/courses.html"
                                },
                                {
                                    "text": "HOME",
                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                    "items": [
                                        {
                                            "text": "about",
                                            "url": "https://preview.colorlib.com/theme/dreams/about.html"
                                        },
                                        {
                                            "text": "instructor",
                                            "url": "https://preview.colorlib.com/theme/dreams/instructor.html"
                                        },
                                        {
                                            "text": "Pricing",
                                            "url": "https://preview.colorlib.com/theme/dreams/pricing.html"
                                        },
                                        {
                                            "text": "FAQ",
                                            "url": "https://preview.colorlib.com/theme/dreams/faq.html"
                                        },
                                        {
                                            "text": "Course Detail",
                                            "url": "https://preview.colorlib.com/theme/dreams/course-detail.html"
                                        },
                                        {
                                            "text": "Blog Detail",
                                            "url": "https://preview.colorlib.com/theme/dreams/blog-detail.html"
                                        }
                                    ]
                                },
                                {
                                    "text": "NEWS",
                                    "url": "https://preview.colorlib.com/theme/dreams/blog.html"
                                },
                                {
                                    "text": "CONTACT",
                                    "url": "https://preview.colorlib.com/theme/dreams/contact.html"
                                }
                            ]
                        }
                    ]
                },
                {
                    "navreight": [
                        {
                            "icon": "fa fa-search search-switch",
                            "klik": {
                                "true": {
                                    "icon": "search-close-switch",
                                    "placeholder": "search here"
                                }
                            }
                        },
                        {
                            "icon": "fa fa-facebook",
                            "url": "https://preview.colorlib.com/theme/dreams/#"
                        },
                        {
                            "icon": "fa fa-twitter",
                            "url": "https://preview.colorlib.com/theme/dreams/#"
                        },
                        {
                            "icon": "fa fa-instagram",
                            "url": "https://preview.colorlib.com/theme/dreams/#"
                        },
                        {
                            "icon": "fa fa-dribbble",
                            "url": "https://preview.colorlib.com/theme/dreams/#"
                        },
                        {
                            "text": "Get Started",
                            "url": "https://preview.colorlib.com/theme/dreams/#"
                        }
                    ]
                }
            ],
            "body": [
                {
                    "breadecrum": [
                        {
                            "bread1": {
                                "url": "https://preview.colorlib.com/theme/dreams/#",
                                "icon": "fa fa-home",
                                "text": "Home"
                            },
                            "bread2": {
                                "text": "Courses"
                            }
                        }
                    ],
                    "aplication-form": [
                        {
                            "aplication-title": {
                                "text1": "Giving Best Options For You",
                                "text2": "Application Form"
                            },
                            "Form-application": [
                                {
                                    "col-1": {
                                        "placeholder": "Your Name"
                                    },
                                    "col-2": {
                                        "placeholder": "Your Email"
                                    },
                                    "col-3": {
                                        "placeholder": "Your Phone"
                                    },
                                    "col-4": {
                                        "placeholder": "Date & time"
                                    },
                                    "col-5": [
                                        {
                                            "optional": {
                                                "option1": "Courses type",
                                                "option2": "Safe driving courses",
                                                "option3": "motorhome Drivers"
                                            },
                                            "select-option": {
                                                "option": "Courses type",
                                                "list": {
                                                    "list1": "Courses type",
                                                    "list2": "safe driving courses",
                                                    "list3": "Motorhome drivers"
                                                }
                                            }
                                        }
                                    ],
                                    "col-6": [
                                        {
                                            "optional": {
                                                "option1": "Car type",
                                                "option2": "hatcback",
                                                "option3": "Sedan",
                                                "option4": "Crossover"
                                            },
                                            "select-option": {
                                                "option": "Car type",
                                                "list": {
                                                    "list1": "Car type",
                                                    "list2": "Sedan",
                                                    "list3": "Crossover"
                                                }
                                            }
                                        }
                                    ],
                                    "button": {
                                        "text": "SEND INQUIRY"
                                    }
                                }
                            ]
                        }
                    ],
                    "courses spad": [
                        {
                            "courses-title": [
                                {
                                    "left": {
                                        "title": {
                                            "text1": "Our great Team",
                                            "text2": "Our instructor"
                                        }
                                    },
                                    "right": {
                                        "button": {
                                            "text": "View all"
                                        }
                                    }
                                }
                            ],
                            "courses-item": [
                                {
                                    "col-1": {
                                        "item-top": {
                                            "img": "img/courses/course-1.jpg",
                                            "text": "Winter driving",
                                            "price": "$ 119"
                                        },
                                        "item-buttom": [
                                            {
                                                "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                            },
                                            {
                                                "button": {
                                                    "url": "#",
                                                    "text": "View detail"
                                                }
                                            }
                                        ]
                                    },
                                    "col-2": {
                                        "item-top": {
                                            "img": "img/courses/course-2.jpg",
                                            "text": "Programa for seniors",
                                            "price": "$ 119"
                                        },
                                        "item-buttom": [
                                            {
                                                "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                            },
                                            {
                                                "button": {
                                                    "url": "#",
                                                    "text": "View detail"
                                                }
                                            }
                                        ]
                                    },
                                    "col-3": {
                                        "item-top": {
                                            "img": "img/courses/course-3.jpg",
                                            "text": "Adult in car lesons",
                                            "price": "$ 119"
                                        },
                                        "item-buttom": [
                                            {
                                                "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                            },
                                            {
                                                "button": {
                                                    "url": "#",
                                                    "text": "View detail"
                                                }
                                            }
                                        ]
                                    },
                                    "col-4": {
                                        "item-top": {
                                            "img": "img/courses/course-4.jpg",
                                            "text": "Teen driver education",
                                            "price": "$ 119"
                                        },
                                        "item-buttom": [
                                            {
                                                "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                            },
                                            {
                                                "button": {
                                                    "url": "#",
                                                    "text": "View detail"
                                                }
                                            }
                                        ]
                                    },
                                    "col-5": {
                                        "item-top": {
                                            "img": "img/courses/course-5.jpg",
                                            "text": "Defensive Driving",
                                            "price": "$ 119"
                                        },
                                        "item-buttom": [
                                            {
                                                "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                            },
                                            {
                                                "button": {
                                                    "url": "#",
                                                    "text": "View detail"
                                                }
                                            }
                                        ]
                                    },
                                    "col-6": {
                                        "item-top": {
                                            "img": "img/courses/course-6.jpg",
                                            "text": "Stick shit lessons",
                                            "price": "$ 119"
                                        },
                                        "item-buttom": [
                                            {
                                                "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                            },
                                            {
                                                "button": {
                                                    "url": "#",
                                                    "text": "View detail"
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    ]
                }
            ],
            "footer": [
                {
                    "body-footer": [
                        {
                            "footer-widget1": [
                                {
                                    "title": {
                                        "text": "COMPANY"
                                    }
                                },
                                {
                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                    "list": {
                                        "list1": "About Us",
                                        "list2": "Company",
                                        "list3": "Press & blog",
                                        "list4": "Privacy Policy",
                                        "list5": "Faq"
                                    }
                                }
                            ],
                            "footer-widget2": [
                                {
                                    "title": {
                                        "text": "Courses"
                                    }
                                },
                                {
                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                    "list": {
                                        "list1": "Winter driving",
                                        "list2": "Program for seniors",
                                        "list3": "Adult in car lesons",
                                        "list4": "Defensive driving",
                                        "list5": "Stick shift lessons"
                                    }
                                }
                            ],
                            "footer-widget3": [
                                {
                                    "title": {
                                        "text": "USEFUL LINKS"
                                    }
                                },
                                {
                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                    "list": {
                                        "list1": "Home",
                                        "list2": "Drupal Themes",
                                        "list3": "Wordpress Themes",
                                        "list4": "Support",
                                        "list5": "Services"
                                    }
                                }
                            ],
                            "footer-about": [
                                {
                                    "logo": {
                                        "img": "img/xfooter-logo.png.pagespeed.ic.m_mZ4QWNCF.webp",
                                        "text": "Address : 15 Division Street, New York, NY 12032, United States of America"
                                    }
                                },
                                {
                                    "list": {
                                        "phone": "+0 (123) 456789",
                                        "Email": "kaseo@gmail.com",
                                        "Fax": "+8 (123) 456 789"
                                    }
                                }
                            ]
                        }
                    ],
                    "footer-finis": {
                        "text": "Copyright © 2022 All rights reserved | This template is made with",
                        "icon": "fa fa-heart",
                        "blank": {
                            "text": "Colorlib",
                            "url": "https://colorlib.com/"
                        }
                    }
                }
            ]
        }

# page pembagian


class Structure(Resource):
    def get(self, element):
        parser = reqparse.RequestParser()
        parser.add_argument('jenisElement', choices=(
            'header', 'body', 'footer'), help='jenis data tidak ditemukan: {error_msg}')
        parser.add_argument(
            'element', help='jenis data tidak ditemukan: {error_msg}')
        args = parser.parse_args()
        print(args)
        # validasi parameter
        if element == 'header':
            # validasi argumen
            if (args.jenisElement != None and args.jenisElement == 'header'):
                if (args.element != None and args.element == 'navleft'):
                    return {
                        "navleft": [
                            {
                                "brand": {
                                    "img": "data:image/webp;base64,UklGRmgDAABXRUJQVlA4TFsDAAAvkEAGEPdAmG1UoPPXu+cUBAJJAvvjLhBIAtxfZ4EAYcF/pAQJ/qNYAQMSJElyFKlpMUz3KGC1mv+/86iMqvtBRP8hSJIbt1lJ1hFEHoAASH8hPbfbCdvHe6LtuOiW+3B5eNsUaFWSEmLchWRWkAq4PT85pq4OvJ680cXC3uaFeRwiAGoRlMXXkRVktiCboZXYWOfeHZ3f6kT3HO4+TyDCxALqJB9kMKwzpF+ezi9xYrp42x7lmeHsIAqjj5K9DNtzKNh/rs5XZY56nAMjhjHOXjpnVwM4MgYPWI4ny90egUe7hZsgvDUBj2yO08VgWsY1AaOnAhwt5MOVLT/+EfzKfpM6kMAfToksECBnGzZYXfIS6s7R6owzZHLdn9+jwfqwzr/hIL1iX1hkwEXA01kQ89EFihkLqAHGZWHfJJb2TT/W+YfUFXxDtZCH/dAb4Nli53wMETNereTcLIxJ02sgqGD5p50HlMH77phkCVDs3NOAJATGAjIAHYYZPMoc1Yf0GF+bpKj0dFshwoPbnLhq9zQgsYFxUu0mLIuSgRPwiH3/cOS0XSjHcJvGt5hy8RlnK4nomJUXXgS1yZavfmHN7lFsR/V5Nj6vqsKMQ3Rkk92Vh2KDBlk1936ww6RvC/FCNQOctun7PJnPNYGYcbOy49QPL/VX8izxEuM38WRxc5YS2NACPJXPg7KRGQ9RNhCLN/GmDXp0dyy5N/9IzQQUtyw0SjsGfpNRshq27Gctfwit/kPxGwzcf1DNLPuFq8NvPUkmxsC2E+Mkkrbc3I4nXRCi94Xt+P0kiElrpXH/BZ6FHSkRrcTYraND4kmzfgB8dy1feU6vOvr9AmPrzRv/cYZASR1bFRsfzO21reAM6AbZ+vg8T/1vqINGM7p1XSiqcw5poKVNBXGjW255e+krttTAshlb8wIpqrcjvGwOnCE3tY6thH2m1F9d1hZYNutb0JIcrbH5YYqdxVOwBBVMn5CGu2wWI9OZwRI73hpdNg9xUrO5aKqDJaiDE5sjbiB/sb+6K68JjAPL5gXOIzlqwLgZafpv4A/ImbJu3tWX+VLHEpPziP0U1LMekgsVLWG1ReljnZNhhobqWr7Lj1O2dH7C9ZilnFdAbhIYsAQddpSxne/dcly7JFoCAA==",
                                    "url": "https://preview.colorlib.com/theme/dreams/index.html"
                                }
                            },
                            {
                                "navbaritems": [
                                    {
                                        "text": "HOME",
                                        "url": "https://preview.colorlib.com/theme/dreams/index.html"
                                    },
                                    {
                                        "text": "COURSES",
                                        "url": "https://preview.colorlib.com/theme/dreams/courses.html"
                                    },
                                    {
                                        "text": "HOME",
                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                        "items": [
                                            {
                                                "text": "about",
                                                "url": "https://preview.colorlib.com/theme/dreams/about.html"
                                            },
                                            {
                                                "text": "instructor",
                                                "url": "https://preview.colorlib.com/theme/dreams/instructor.html"
                                            },
                                            {
                                                "text": "Pricing",
                                                "url": "https://preview.colorlib.com/theme/dreams/pricing.html"
                                            },
                                            {
                                                "text": "FAQ",
                                                "url": "https://preview.colorlib.com/theme/dreams/faq.html"
                                            },
                                            {
                                                "text": "Course Detail",
                                                "url": "https://preview.colorlib.com/theme/dreams/course-detail.html"
                                            },
                                            {
                                                "text": "Blog Detail",
                                                "url": "https://preview.colorlib.com/theme/dreams/blog-detail.html"
                                            }
                                        ]
                                    },
                                    {
                                        "text": "NEWS",
                                        "url": "https://preview.colorlib.com/theme/dreams/blog.html"
                                    },
                                    {
                                        "text": "CONTACT",
                                        "url": "https://preview.colorlib.com/theme/dreams/contact.html"
                                    }
                                ]
                            }
                        ]
                    }
                elif (args.element != None and args.element == 'navright'):
                    return {
                        "navright": [
                            {
                                "icon": "fa fa-search search-switch",
                                "klik": {
                                    "true": {
                                        "icon": "search-close-switch",
                                        "placeholder": "search here"
                                    }
                                }
                            },
                            {
                                "icon": "fa fa-facebook",
                                "url": "https://preview.colorlib.com/theme/dreams/#"
                            },
                            {
                                "icon": "fa fa-twitter",
                                "url": "https://preview.colorlib.com/theme/dreams/#"
                            },
                            {
                                "icon": "fa fa-instagram",
                                "url": "https://preview.colorlib.com/theme/dreams/#"
                            },
                            {
                                "icon": "fa fa-dribbble",
                                "url": "https://preview.colorlib.com/theme/dreams/#"
                            },
                            {
                                "text": "Get Started",
                                "url": "https://preview.colorlib.com/theme/dreams/#"
                            }
                        ]
                    }
            else:
                return {
                    "header": [
                        {
                            "navleft": [
                                {
                                    "brand": {
                                        "img": "data:image/webp;base64,UklGRmgDAABXRUJQVlA4TFsDAAAvkEAGEPdAmG1UoPPXu+cUBAJJAvvjLhBIAtxfZ4EAYcF/pAQJ/qNYAQMSJElyFKlpMUz3KGC1mv+/86iMqvtBRP8hSJIbt1lJ1hFEHoAASH8hPbfbCdvHe6LtuOiW+3B5eNsUaFWSEmLchWRWkAq4PT85pq4OvJ680cXC3uaFeRwiAGoRlMXXkRVktiCboZXYWOfeHZ3f6kT3HO4+TyDCxALqJB9kMKwzpF+ezi9xYrp42x7lmeHsIAqjj5K9DNtzKNh/rs5XZY56nAMjhjHOXjpnVwM4MgYPWI4ny90egUe7hZsgvDUBj2yO08VgWsY1AaOnAhwt5MOVLT/+EfzKfpM6kMAfToksECBnGzZYXfIS6s7R6owzZHLdn9+jwfqwzr/hIL1iX1hkwEXA01kQ89EFihkLqAHGZWHfJJb2TT/W+YfUFXxDtZCH/dAb4Nli53wMETNereTcLIxJ02sgqGD5p50HlMH77phkCVDs3NOAJATGAjIAHYYZPMoc1Yf0GF+bpKj0dFshwoPbnLhq9zQgsYFxUu0mLIuSgRPwiH3/cOS0XSjHcJvGt5hy8RlnK4nomJUXXgS1yZavfmHN7lFsR/V5Nj6vqsKMQ3Rkk92Vh2KDBlk1936ww6RvC/FCNQOctun7PJnPNYGYcbOy49QPL/VX8izxEuM38WRxc5YS2NACPJXPg7KRGQ9RNhCLN/GmDXp0dyy5N/9IzQQUtyw0SjsGfpNRshq27Gctfwit/kPxGwzcf1DNLPuFq8NvPUkmxsC2E+Mkkrbc3I4nXRCi94Xt+P0kiElrpXH/BZ6FHSkRrcTYraND4kmzfgB8dy1feU6vOvr9AmPrzRv/cYZASR1bFRsfzO21reAM6AbZ+vg8T/1vqINGM7p1XSiqcw5poKVNBXGjW255e+krttTAshlb8wIpqrcjvGwOnCE3tY6thH2m1F9d1hZYNutb0JIcrbH5YYqdxVOwBBVMn5CGu2wWI9OZwRI73hpdNg9xUrO5aKqDJaiDE5sjbiB/sb+6K68JjAPL5gXOIzlqwLgZafpv4A/ImbJu3tWX+VLHEpPziP0U1LMekgsVLWG1ReljnZNhhobqWr7Lj1O2dH7C9ZilnFdAbhIYsAQddpSxne/dcly7JFoCAA==",
                                        "url": "https://preview.colorlib.com/theme/dreams/index.html"
                                    }
                                },
                                {
                                    "navbaritems": [
                                        {
                                            "text": "HOME",
                                            "url": "https://preview.colorlib.com/theme/dreams/index.html"
                                        },
                                        {
                                            "text": "COURSES",
                                            "url": "https://preview.colorlib.com/theme/dreams/courses.html"
                                        },
                                        {
                                            "text": "HOME",
                                            "url": "https://preview.colorlib.com/theme/dreams/#",
                                            "items": [
                                                {
                                                    "text": "about",
                                                    "url": "https://preview.colorlib.com/theme/dreams/about.html"
                                                },
                                                {
                                                    "text": "instructor",
                                                    "url": "https://preview.colorlib.com/theme/dreams/instructor.html"
                                                },
                                                {
                                                    "text": "Pricing",
                                                    "url": "https://preview.colorlib.com/theme/dreams/pricing.html"
                                                },
                                                {
                                                    "text": "FAQ",
                                                    "url": "https://preview.colorlib.com/theme/dreams/faq.html"
                                                },
                                                {
                                                    "text": "Course Detail",
                                                    "url": "https://preview.colorlib.com/theme/dreams/course-detail.html"
                                                },
                                                {
                                                    "text": "Blog Detail",
                                                    "url": "https://preview.colorlib.com/theme/dreams/blog-detail.html"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "NEWS",
                                            "url": "https://preview.colorlib.com/theme/dreams/blog.html"
                                        },
                                        {
                                            "text": "CONTACT",
                                            "url": "https://preview.colorlib.com/theme/dreams/contact.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "navright": [
                                {
                                    "icon": "fa fa-search search-switch",
                                    "klik": {
                                        "true": {
                                            "icon": "search-close-switch",
                                            "placeholder": "search here"
                                        }
                                    }
                                },
                                {
                                    "icon": "fa fa-facebook",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                },
                                {
                                    "icon": "fa fa-twitter",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                },
                                {
                                    "icon": "fa fa-instagram",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                },
                                {
                                    "icon": "fa fa-dribbble",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                },
                                {
                                    "text": "Get Started",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                }
                            ]
                        }
                    ]
                }
        elif element == 'body':
            if(args.jenisElement != None and args.jenisElement == 'body'):
                if(args.element != None and args.element == 'hero_benner'):
                    return{
                        "hero_benner": {
                            "bacground_image": "img/hero-bg.jpg",
                            "hero_text": [
                                {
                                    "text1": "BEST OPTIONS FOR YOU",
                                    "text2": "DRIVE SAFE & GET LICENSE",
                                    "hero_text_pilih": [
                                        {
                                            "text": "Contact Us",
                                            "url": "https://preview.colorlib.com/theme/dreams/#"
                                        },
                                        {
                                            "text": "See Courses",
                                            "url": "https://preview.colorlib.com/theme/dreams/#"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                elif(args.element != None and args.element == 'feature'):
                    return{
                        "feature": [
                            {
                                "feactur_text": {
                                    "text1": "Why choose us ?",
                                    "text2": "Our feature",
                                    "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua viverra maecenas facilisis"
                                }
                            },
                            {
                                "feactur_item": [
                                    {
                                        "item1": {
                                            "img": "img/feature/xfeature-1.png.pagespeed.ic.22dCgiNvOu.webp",
                                            "text": "Unlimited Car Support"
                                        },
                                        "item2": {
                                            "img": "img/feature/xfeature-2.png.pagespeed.ic.r1evg5EssL.webp",
                                            "text": "Driving School Insures"
                                        },
                                        "item3": {
                                            "img": "img/feature/xfeature-3.png.pagespeed.ic.ZNUFBwu5wI.webp",
                                            "text": "Any Time Any Location"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                elif(args.element != None and args.element == 'about-vidio'):
                    return{
                        "about-vidio": [
                            {
                                "vidio": {
                                    "img-bacground-vidio": "img/video-bg.jpg",
                                    "button": "btn play-vidio",
                                    "url-youtobe": "https://www.youtube.com/watch?v=bGuHgRQSEuk"
                                },
                                "about_vidio_text": [
                                    {
                                        "title": {
                                            "text1": "Welcome to Online trafic school",
                                            "text2": "looking for lessons?"
                                        },
                                        "paragraf": {
                                            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum vidnas accumsan lacus velfacilisis.",
                                            "button": {
                                                "text": "Learn more",
                                                "url": "https://preview.colorlib.com/theme/dreams/#"
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                elif(args.element != None and args.element == 'application-form'):
                    return{
                        "application-form": [
                            {
                                "title": {
                                    "text1": "Giving Best Option For You",
                                    "text2": "Application Form"
                                },
                                "formulir": [
                                    {
                                        "input1": {
                                            "placeholder": "Your name"
                                        },
                                        "input2": {
                                            "placeholder": "Your Email"
                                        },
                                        "input3": {
                                            "placeholder": "Your Phone"
                                        },
                                        "input5": {
                                            "placeholder": "Date & time"
                                        },
                                        "option-item1": [
                                            {
                                                "options": {
                                                    "option1": "Courses type",
                                                    "option2": "Safe Driving Courses",
                                                    "option3": "Motorhome Drivers"
                                                },
                                                "list": {
                                                    "list1": "Courses type",
                                                    "list2": "Safe Driving Courses",
                                                    "list3": "Motorhome Drivers"
                                                }
                                            }
                                        ],
                                        "option-item2": [
                                            {
                                                "options": {
                                                    "option1": "Car type",
                                                    "option2": "Hatcback",
                                                    "option3": "Sedan"
                                                },
                                                "list": {
                                                    "list1": "Car type",
                                                    "list2": "Hatcback",
                                                    "list3": "Sedan"
                                                }
                                            }
                                        ],
                                        "button-send": {
                                            "text": "SEND INQUIRY"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                elif(args.element != None and args.element == 'application-form'):
                    return{
                        "pricing": [
                            {
                                "pricing-title": {
                                    "text1": "Get Spesial Offer",
                                    "text2": "Our Pricing"
                                },
                                "pricing-item1": [
                                    {
                                        "text-top": "20% off",
                                        "price": "$ 199",
                                        "text": "Personal Driving"
                                    },
                                    {
                                        "list-item-pricing": {
                                            "list1": "Full course theory",
                                            "list2": "Full driving course",
                                            "list3": "Training in first aid",
                                            "list4": "Practical sessions",
                                            "list5": "Psychological support"
                                        }
                                    },
                                    {
                                        "text": "GET STARTED",
                                        "url": "https://preview.colorlib.com/theme/dreams/#"
                                    }
                                ],
                                "pricing-item2": [
                                    {
                                        "text-top": "20% off",
                                        "price": "$ 379",
                                        "text": "Power Booster"
                                    },
                                    {
                                        "list-item-pricing": {
                                            "list1": "Full course theory",
                                            "list2": "Full driving course",
                                            "list3": "Training in first aid",
                                            "list4": "Practical sessions",
                                            "list5": "Psychological support"
                                        }
                                    },
                                    {
                                        "text": "GET STARTED",
                                        "url": "https://preview.colorlib.com/theme/dreams/#"
                                    }
                                ],
                                "pricing-item3": [
                                    {
                                        "text-top": "20% off",
                                        "price": "$ 259",
                                        "text": "Freight Driving"
                                    },
                                    {
                                        "list-item-pricing": {
                                            "list1": "Full course theory",
                                            "list2": "Full driving course",
                                            "list3": "Training in first aid",
                                            "list4": "Practical sessions",
                                            "list5": "Psychological support"
                                        }
                                    },
                                    {
                                        "text": "GET STARTED",
                                        "url": "https://preview.colorlib.com/theme/dreams/?#"
                                    }
                                ]
                            }
                        ]
                    }
                else:
                    return{
                        "team": [
                            {
                                "team-title": {
                                    "text1": "Our Great Team",
                                    "text2": "Our Instructor",
                                    "btn-team-all": {
                                        "text": "View all",
                                        "url": "https://preview.colorlib.com/theme/dreams/#"
                                    }
                                },
                                "team-item": [
                                    {
                                        "team-item1": [
                                            {
                                                "item-img": {
                                                    "img": "img/team/xteam-1.png.pagespeed.ic.cHiltCofrK.webp"
                                                },
                                                "item-text": {
                                                    "text1": "DAVID WARNER",
                                                    "text2": "Instructor",
                                                    "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                },
                                                "item-social": {
                                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                                    "icon": {
                                                        "icon1": "fa fa-fecebook",
                                                        "icon2": "fa fa-twitter",
                                                        "icon3": "fa fa-instagram",
                                                        "icon4": "fa fa-dribbble"
                                                    }
                                                }
                                            }
                                        ],
                                        "team-item2": [
                                            {
                                                "item-img": {
                                                    "img": "img/team/xteam-2.png.pagespeed.ic.dZB3yfmD0i.webp"
                                                },
                                                "item-text": {
                                                    "text1": "DAVID WARNER",
                                                    "text2": "Instructor",
                                                    "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                },
                                                "item-social": {
                                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                                    "icon": {
                                                        "icon1": "fa fa-fecebook",
                                                        "icon2": "fa fa-twitter",
                                                        "icon3": "fa fa-instagram",
                                                        "icon4": "fa fa-dribbble"
                                                    }
                                                }
                                            }
                                        ],
                                        "team-item3": [
                                            {
                                                "item-img": {
                                                    "img": "img/team/xteam-3.png.pagespeed.ic.AOhA2y9pBh.webp"
                                                },
                                                "item-text": {
                                                    "text1": "DAVID WARNER",
                                                    "text2": "Instructor",
                                                    "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                },
                                                "item-social": {
                                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                                    "icon": {
                                                        "icon1": "fa fa-fecebook",
                                                        "icon2": "fa fa-twitter",
                                                        "icon3": "fa fa-instagram",
                                                        "icon4": "fa fa-dribbble"
                                                    }
                                                }
                                            }
                                        ],
                                        "team-item4": [
                                            {
                                                "item-img": {
                                                    "img": "img/team/xteam-4.png.pagespeed.ic.x98B_rqu1y.webp"
                                                },
                                                "item-text": {
                                                    "text1": "DAVID WARNER",
                                                    "text2": "Instructor",
                                                    "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                },
                                                "item-social": {
                                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                                    "icon": {
                                                        "icon1": "fa fa-fecebook",
                                                        "icon2": "fa fa-twitter",
                                                        "icon3": "fa fa-instagram",
                                                        "icon4": "fa fa-dribbble"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
            else:
                return {
                    "body": [
                        {
                            "hero_benner": {
                                "bacground_image": "img/hero-bg.jpg",
                                "hero_text": [
                                    {
                                        "text1": "BEST OPTIONS FOR YOU",
                                        "text2": "DRIVE SAFE & GET LICENSE",
                                        "hero_text_pilih": [
                                            {
                                                "text": "Contact Us",
                                                "url": "https://preview.colorlib.com/theme/dreams/#"
                                            },
                                            {
                                                "text": "See Courses",
                                                "url": "https://preview.colorlib.com/theme/dreams/#"
                                            }
                                        ]
                                    }
                                ]
                            },
                            "feature": [
                                {
                                    "feactur_text": {
                                        "text1": "Why choose us ?",
                                        "text2": "Our feature",
                                        "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua viverra maecenas facilisis"
                                    }
                                },
                                {
                                    "feactur_item": [
                                        {
                                            "item1": {
                                                "img": "img/feature/xfeature-1.png.pagespeed.ic.22dCgiNvOu.webp",
                                                "text": "Unlimited Car Support"
                                            },
                                            "item2": {
                                                "img": "img/feature/xfeature-2.png.pagespeed.ic.r1evg5EssL.webp",
                                                "text": "Driving School Insures"
                                            },
                                            "item3": {
                                                "img": "img/feature/xfeature-3.png.pagespeed.ic.ZNUFBwu5wI.webp",
                                                "text": "Any Time Any Location"
                                            }
                                        }
                                    ]
                                }
                            ],
                            "about-vidio": [
                                {
                                    "vidio": {
                                        "img-bacground-vidio": "img/video-bg.jpg",
                                        "button": "btn play-vidio",
                                        "url-youtobe": "https://www.youtube.com/watch?v=bGuHgRQSEuk"
                                    },
                                    "about_vidio_text": [
                                        {
                                            "title": {
                                                "text1": "Welcome to Online trafic school",
                                                "text2": "looking for lessons?"
                                            },
                                            "paragraf": {
                                                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum vidnas accumsan lacus velfacilisis.",
                                                "button": {
                                                    "text": "Learn more",
                                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                                }
                                            }
                                        }
                                    ]
                                }
                            ],
                            "application-form": [
                                {
                                    "title": {
                                        "text1": "Giving Best Option For You",
                                        "text2": "Application Form"
                                    },
                                    "formulir": [
                                        {
                                            "input1": {
                                                "placeholder": "Your name"
                                            },
                                            "input2": {
                                                "placeholder": "Your Email"
                                            },
                                            "input3": {
                                                "placeholder": "Your Phone"
                                            },
                                            "input5": {
                                                "placeholder": "Date & time"
                                            },
                                            "option-item1": [
                                                {
                                                    "options": {
                                                        "option1": "Courses type",
                                                        "option2": "Safe Driving Courses",
                                                        "option3": "Motorhome Drivers"
                                                    },
                                                    "list": {
                                                        "list1": "Courses type",
                                                        "list2": "Safe Driving Courses",
                                                        "list3": "Motorhome Drivers"
                                                    }
                                                }
                                            ],
                                            "option-item2": [
                                                {
                                                    "options": {
                                                        "option1": "Car type",
                                                        "option2": "Hatcback",
                                                        "option3": "Sedan"
                                                    },
                                                    "list": {
                                                        "list1": "Car type",
                                                        "list2": "Hatcback",
                                                        "list3": "Sedan"
                                                    }
                                                }
                                            ],
                                            "button-send": {
                                                "text": "SEND INQUIRY"
                                            }
                                        }
                                    ]
                                }
                            ],
                            "pricing": [
                                {
                                    "pricing-title": {
                                        "text1": "Get Spesial Offer",
                                        "text2": "Our Pricing"
                                    },
                                    "pricing-item1": [
                                        {
                                            "text-top": "20% off",
                                            "price": "$ 199",
                                            "text": "Personal Driving"
                                        },
                                        {
                                            "list-item-pricing": {
                                                "list1": "Full course theory",
                                                "list2": "Full driving course",
                                                "list3": "Training in first aid",
                                                "list4": "Practical sessions",
                                                "list5": "Psychological support"
                                            }
                                        },
                                        {
                                            "text": "GET STARTED",
                                            "url": "https://preview.colorlib.com/theme/dreams/#"
                                        }
                                    ],
                                    "pricing-item2": [
                                        {
                                            "text-top": "20% off",
                                            "price": "$ 379",
                                            "text": "Power Booster"
                                        },
                                        {
                                            "list-item-pricing": {
                                                "list1": "Full course theory",
                                                "list2": "Full driving course",
                                                "list3": "Training in first aid",
                                                "list4": "Practical sessions",
                                                "list5": "Psychological support"
                                            }
                                        },
                                        {
                                            "text": "GET STARTED",
                                            "url": "https://preview.colorlib.com/theme/dreams/#"
                                        }
                                    ],
                                    "pricing-item3": [
                                        {
                                            "text-top": "20% off",
                                            "price": "$ 259",
                                            "text": "Freight Driving"
                                        },
                                        {
                                            "list-item-pricing": {
                                                "list1": "Full course theory",
                                                "list2": "Full driving course",
                                                "list3": "Training in first aid",
                                                "list4": "Practical sessions",
                                                "list5": "Psychological support"
                                            }
                                        },
                                        {
                                            "text": "GET STARTED",
                                            "url": "https://preview.colorlib.com/theme/dreams/?#"
                                        }
                                    ]
                                }
                            ],
                            "team": [
                                {
                                    "team-title": {
                                        "text1": "Our Great Team",
                                        "text2": "Our Instructor",
                                        "btn-team-all": {
                                            "text": "View all",
                                            "url": "https://preview.colorlib.com/theme/dreams/#"
                                        }
                                    },
                                    "team-item": [
                                        {
                                            "team-item1": [
                                                {
                                                    "item-img": {
                                                        "img": "img/team/xteam-1.png.pagespeed.ic.cHiltCofrK.webp"
                                                    },
                                                    "item-text": {
                                                        "text1": "DAVID WARNER",
                                                        "text2": "Instructor",
                                                        "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                    },
                                                    "item-social": {
                                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                                        "icon": {
                                                            "icon1": "fa fa-fecebook",
                                                            "icon2": "fa fa-twitter",
                                                            "icon3": "fa fa-instagram",
                                                            "icon4": "fa fa-dribbble"
                                                        }
                                                    }
                                                }
                                            ],
                                            "team-item2": [
                                                {
                                                    "item-img": {
                                                        "img": "img/team/xteam-2.png.pagespeed.ic.dZB3yfmD0i.webp"
                                                    },
                                                    "item-text": {
                                                        "text1": "DAVID WARNER",
                                                        "text2": "Instructor",
                                                        "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                    },
                                                    "item-social": {
                                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                                        "icon": {
                                                            "icon1": "fa fa-fecebook",
                                                            "icon2": "fa fa-twitter",
                                                            "icon3": "fa fa-instagram",
                                                            "icon4": "fa fa-dribbble"
                                                        }
                                                    }
                                                }
                                            ],
                                            "team-item3": [
                                                {
                                                    "item-img": {
                                                        "img": "img/team/xteam-3.png.pagespeed.ic.AOhA2y9pBh.webp"
                                                    },
                                                    "item-text": {
                                                        "text1": "DAVID WARNER",
                                                        "text2": "Instructor",
                                                        "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                    },
                                                    "item-social": {
                                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                                        "icon": {
                                                            "icon1": "fa fa-fecebook",
                                                            "icon2": "fa fa-twitter",
                                                            "icon3": "fa fa-instagram",
                                                            "icon4": "fa fa-dribbble"
                                                        }
                                                    }
                                                }
                                            ],
                                            "team-item4": [
                                                {
                                                    "item-img": {
                                                        "img": "img/team/xteam-4.png.pagespeed.ic.x98B_rqu1y.webp"
                                                    },
                                                    "item-text": {
                                                        "text1": "DAVID WARNER",
                                                        "text2": "Instructor",
                                                        "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                    },
                                                    "item-social": {
                                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                                        "icon": {
                                                            "icon1": "fa fa-fecebook",
                                                            "icon2": "fa fa-twitter",
                                                            "icon3": "fa fa-instagram",
                                                            "icon4": "fa fa-dribbble"
                                                        }
                                                    }
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                }
        elif element == 'footer':
            if(args.jenisElement != None and args.jenisElement == 'footer'):
                if(args.element != None and args.element == 'body-footer'):
                    return{
                        "body-footer": [
                            {
                                "footer-widget1": [
                                    {
                                        "title": {
                                            "text": "COMPANY"
                                        }
                                    },
                                    {
                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                        "list": {
                                            "list1": "About Us",
                                            "list2": "Company",
                                            "list3": "Press & blog",
                                            "list4": "Privacy Policy",
                                            "list5": "Faq"
                                        }
                                    }
                                ],
                                "footer-widget2": [
                                    {
                                        "title": {
                                            "text": "Courses"
                                        }
                                    },
                                    {
                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                        "list": {
                                            "list1": "Winter driving",
                                            "list2": "Program for seniors",
                                            "list3": "Adult in car lesons",
                                            "list4": "Defensive driving",
                                            "list5": "Stick shift lessons"
                                        }
                                    }
                                ],
                                "footer-widget3": [
                                    {
                                        "title": {
                                            "text": "USEFUL LINKS"
                                        }
                                    },
                                    {
                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                        "list": {
                                            "list1": "Home",
                                            "list2": "Drupal Themes",
                                            "list3": "Wordpress Themes",
                                            "list4": "Support",
                                            "list5": "Services"
                                        }
                                    }
                                ],
                                "footer-about": [
                                    {
                                        "logo": {
                                            "img": "img/xfooter-logo.png.pagespeed.ic.m_mZ4QWNCF.webp",
                                            "text": "Address : 15 Division Street, New York, NY 12032, United States of America"
                                        }
                                    },
                                    {
                                        "list": {
                                            "phone": "+0 (123) 456789",
                                            "Email": "kaseo@gmail.com",
                                            "Fax": "+8 (123) 456 789"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                else:
                    return{
                        "footer-finis": {
                            "text": "Copyright © 2022 All rights reserved | This template is made with",
                            "icon": "fa fa-heart",
                            "blank": {
                                "text": "Colorlib",
                                "url": "https://colorlib.com/"
                            }
                        }
                    }
            else:
                return {
                    "footer": [
                        {
                            "body-footer": [
                                {
                                    "footer-widget1": [
                                        {
                                            "title": {
                                                "text": "COMPANY"
                                            }
                                        },
                                        {
                                            "url": "https://preview.colorlib.com/theme/dreams/#",
                                            "list": {
                                                "list1": "About Us",
                                                "list2": "Company",
                                                "list3": "Press & blog",
                                                "list4": "Privacy Policy",
                                                "list5": "Faq"
                                            }
                                        }
                                    ],
                                    "footer-widget2": [
                                        {
                                            "title": {
                                                "text": "Courses"
                                            }
                                        },
                                        {
                                            "url": "https://preview.colorlib.com/theme/dreams/#",
                                            "list": {
                                                "list1": "Winter driving",
                                                "list2": "Program for seniors",
                                                "list3": "Adult in car lesons",
                                                "list4": "Defensive driving",
                                                "list5": "Stick shift lessons"
                                            }
                                        }
                                    ],
                                    "footer-widget3": [
                                        {
                                            "title": {
                                                "text": "USEFUL LINKS"
                                            }
                                        },
                                        {
                                            "url": "https://preview.colorlib.com/theme/dreams/#",
                                            "list": {
                                                "list1": "Home",
                                                "list2": "Drupal Themes",
                                                "list3": "Wordpress Themes",
                                                "list4": "Support",
                                                "list5": "Services"
                                            }
                                        }
                                    ],
                                    "footer-about": [
                                        {
                                            "logo": {
                                                "img": "img/xfooter-logo.png.pagespeed.ic.m_mZ4QWNCF.webp",
                                                "text": "Address : 15 Division Street, New York, NY 12032, United States of America"
                                            }
                                        },
                                        {
                                            "list": {
                                                "phone": "+0 (123) 456789",
                                                "Email": "kaseo@gmail.com",
                                                "Fax": "+8 (123) 456 789"
                                            }
                                        }
                                    ]
                                }
                            ],
                            "footer-finis": {
                                "text": "Copyright © 2022 All rights reserved | This template is made with",
                                "icon": "fa fa-heart",
                                "blank": {
                                    "text": "Colorlib",
                                    "url": "https://colorlib.com/"
                                }
                            }
                        }
                    ]
                }
        else:
            return "not found"


class Bagian(Resource):
    def get(self, element):
        parser = reqparse.RequestParser()
        parser.add_argument('jenisElement', choices=(
            'header', 'body', 'footer'), help='jenis data tidak ditemukan: {error_msg}')
        parser.add_argument(
            'element', help='jenis data tidak ditemukan: {error_msg}')
        args = parser.parse_args()
        print(args)
        # validasi parameter
        if element == 'header':
            # validasi argumen
            if (args.jenisElement != None and args.jenisElement == 'header'):
                if (args.element != None and args.element == 'navleft'):
                    return {
                        "navleft": [
                            {
                                "brand": {
                                    "img": "data:image/webp;base64,UklGRmgDAABXRUJQVlA4TFsDAAAvkEAGEPdAmG1UoPPXu+cUBAJJAvvjLhBIAtxfZ4EAYcF/pAQJ/qNYAQMSJElyFKlpMUz3KGC1mv+/86iMqvtBRP8hSJIbt1lJ1hFEHoAASH8hPbfbCdvHe6LtuOiW+3B5eNsUaFWSEmLchWRWkAq4PT85pq4OvJ680cXC3uaFeRwiAGoRlMXXkRVktiCboZXYWOfeHZ3f6kT3HO4+TyDCxALqJB9kMKwzpF+ezi9xYrp42x7lmeHsIAqjj5K9DNtzKNh/rs5XZY56nAMjhjHOXjpnVwM4MgYPWI4ny90egUe7hZsgvDUBj2yO08VgWsY1AaOnAhwt5MOVLT/+EfzKfpM6kMAfToksECBnGzZYXfIS6s7R6owzZHLdn9+jwfqwzr/hIL1iX1hkwEXA01kQ89EFihkLqAHGZWHfJJb2TT/W+YfUFXxDtZCH/dAb4Nli53wMETNereTcLIxJ02sgqGD5p50HlMH77phkCVDs3NOAJATGAjIAHYYZPMoc1Yf0GF+bpKj0dFshwoPbnLhq9zQgsYFxUu0mLIuSgRPwiH3/cOS0XSjHcJvGt5hy8RlnK4nomJUXXgS1yZavfmHN7lFsR/V5Nj6vqsKMQ3Rkk92Vh2KDBlk1936ww6RvC/FCNQOctun7PJnPNYGYcbOy49QPL/VX8izxEuM38WRxc5YS2NACPJXPg7KRGQ9RNhCLN/GmDXp0dyy5N/9IzQQUtyw0SjsGfpNRshq27Gctfwit/kPxGwzcf1DNLPuFq8NvPUkmxsC2E+Mkkrbc3I4nXRCi94Xt+P0kiElrpXH/BZ6FHSkRrcTYraND4kmzfgB8dy1feU6vOvr9AmPrzRv/cYZASR1bFRsfzO21reAM6AbZ+vg8T/1vqINGM7p1XSiqcw5poKVNBXGjW255e+krttTAshlb8wIpqrcjvGwOnCE3tY6thH2m1F9d1hZYNutb0JIcrbH5YYqdxVOwBBVMn5CGu2wWI9OZwRI73hpdNg9xUrO5aKqDJaiDE5sjbiB/sb+6K68JjAPL5gXOIzlqwLgZafpv4A/ImbJu3tWX+VLHEpPziP0U1LMekgsVLWG1ReljnZNhhobqWr7Lj1O2dH7C9ZilnFdAbhIYsAQddpSxne/dcly7JFoCAA==",
                                    "url": "https://preview.colorlib.com/theme/dreams/index.html"
                                }
                            },
                            {
                                "navbaritems": [
                                    {
                                        "text": "HOME",
                                        "url": "https://preview.colorlib.com/theme/dreams/index.html"
                                    },
                                    {
                                        "text": "COURSES",
                                        "url": "https://preview.colorlib.com/theme/dreams/courses.html"
                                    },
                                    {
                                        "text": "HOME",
                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                        "items": [
                                            {
                                                "text": "about",
                                                "url": "https://preview.colorlib.com/theme/dreams/about.html"
                                            },
                                            {
                                                "text": "instructor",
                                                "url": "https://preview.colorlib.com/theme/dreams/instructor.html"
                                            },
                                            {
                                                "text": "Pricing",
                                                "url": "https://preview.colorlib.com/theme/dreams/pricing.html"
                                            },
                                            {
                                                "text": "FAQ",
                                                "url": "https://preview.colorlib.com/theme/dreams/faq.html"
                                            },
                                            {
                                                "text": "Course Detail",
                                                "url": "https://preview.colorlib.com/theme/dreams/course-detail.html"
                                            },
                                            {
                                                "text": "Blog Detail",
                                                "url": "https://preview.colorlib.com/theme/dreams/blog-detail.html"
                                            }
                                        ]
                                    },
                                    {
                                        "text": "NEWS",
                                        "url": "https://preview.colorlib.com/theme/dreams/blog.html"
                                    },
                                    {
                                        "text": "CONTACT",
                                        "url": "https://preview.colorlib.com/theme/dreams/contact.html"
                                    }
                                ]
                            }
                        ]
                    }
                elif (args.element != None and args.element == 'navright'):
                    return {
                        "navright": [
                            {
                                "icon": "fa fa-search search-switch",
                                "klik": {
                                    "true": {
                                        "icon": "search-close-switch",
                                        "placeholder": "search here"
                                    }
                                }
                            },
                            {
                                "icon": "fa fa-facebook",
                                "url": "https://preview.colorlib.com/theme/dreams/#"
                            },
                            {
                                "icon": "fa fa-twitter",
                                "url": "https://preview.colorlib.com/theme/dreams/#"
                            },
                            {
                                "icon": "fa fa-instagram",
                                "url": "https://preview.colorlib.com/theme/dreams/#"
                            },
                            {
                                "icon": "fa fa-dribbble",
                                "url": "https://preview.colorlib.com/theme/dreams/#"
                            },
                            {
                                "text": "Get Started",
                                "url": "https://preview.colorlib.com/theme/dreams/#"
                            }
                        ]
                    }
            else:
                return {
                    "header": [
                        {
                            "navleft": [
                                {
                                    "brand": {
                                        "img": "data:image/webp;base64,UklGRmgDAABXRUJQVlA4TFsDAAAvkEAGEPdAmG1UoPPXu+cUBAJJAvvjLhBIAtxfZ4EAYcF/pAQJ/qNYAQMSJElyFKlpMUz3KGC1mv+/86iMqvtBRP8hSJIbt1lJ1hFEHoAASH8hPbfbCdvHe6LtuOiW+3B5eNsUaFWSEmLchWRWkAq4PT85pq4OvJ680cXC3uaFeRwiAGoRlMXXkRVktiCboZXYWOfeHZ3f6kT3HO4+TyDCxALqJB9kMKwzpF+ezi9xYrp42x7lmeHsIAqjj5K9DNtzKNh/rs5XZY56nAMjhjHOXjpnVwM4MgYPWI4ny90egUe7hZsgvDUBj2yO08VgWsY1AaOnAhwt5MOVLT/+EfzKfpM6kMAfToksECBnGzZYXfIS6s7R6owzZHLdn9+jwfqwzr/hIL1iX1hkwEXA01kQ89EFihkLqAHGZWHfJJb2TT/W+YfUFXxDtZCH/dAb4Nli53wMETNereTcLIxJ02sgqGD5p50HlMH77phkCVDs3NOAJATGAjIAHYYZPMoc1Yf0GF+bpKj0dFshwoPbnLhq9zQgsYFxUu0mLIuSgRPwiH3/cOS0XSjHcJvGt5hy8RlnK4nomJUXXgS1yZavfmHN7lFsR/V5Nj6vqsKMQ3Rkk92Vh2KDBlk1936ww6RvC/FCNQOctun7PJnPNYGYcbOy49QPL/VX8izxEuM38WRxc5YS2NACPJXPg7KRGQ9RNhCLN/GmDXp0dyy5N/9IzQQUtyw0SjsGfpNRshq27Gctfwit/kPxGwzcf1DNLPuFq8NvPUkmxsC2E+Mkkrbc3I4nXRCi94Xt+P0kiElrpXH/BZ6FHSkRrcTYraND4kmzfgB8dy1feU6vOvr9AmPrzRv/cYZASR1bFRsfzO21reAM6AbZ+vg8T/1vqINGM7p1XSiqcw5poKVNBXGjW255e+krttTAshlb8wIpqrcjvGwOnCE3tY6thH2m1F9d1hZYNutb0JIcrbH5YYqdxVOwBBVMn5CGu2wWI9OZwRI73hpdNg9xUrO5aKqDJaiDE5sjbiB/sb+6K68JjAPL5gXOIzlqwLgZafpv4A/ImbJu3tWX+VLHEpPziP0U1LMekgsVLWG1ReljnZNhhobqWr7Lj1O2dH7C9ZilnFdAbhIYsAQddpSxne/dcly7JFoCAA==",
                                        "url": "https://preview.colorlib.com/theme/dreams/index.html"
                                    }
                                },
                                {
                                    "navbaritems": [
                                        {
                                            "text": "HOME",
                                            "url": "https://preview.colorlib.com/theme/dreams/index.html"
                                        },
                                        {
                                            "text": "COURSES",
                                            "url": "https://preview.colorlib.com/theme/dreams/courses.html"
                                        },
                                        {
                                            "text": "HOME",
                                            "url": "https://preview.colorlib.com/theme/dreams/#",
                                            "items": [
                                                {
                                                    "text": "about",
                                                    "url": "https://preview.colorlib.com/theme/dreams/about.html"
                                                },
                                                {
                                                    "text": "instructor",
                                                    "url": "https://preview.colorlib.com/theme/dreams/instructor.html"
                                                },
                                                {
                                                    "text": "Pricing",
                                                    "url": "https://preview.colorlib.com/theme/dreams/pricing.html"
                                                },
                                                {
                                                    "text": "FAQ",
                                                    "url": "https://preview.colorlib.com/theme/dreams/faq.html"
                                                },
                                                {
                                                    "text": "Course Detail",
                                                    "url": "https://preview.colorlib.com/theme/dreams/course-detail.html"
                                                },
                                                {
                                                    "text": "Blog Detail",
                                                    "url": "https://preview.colorlib.com/theme/dreams/blog-detail.html"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "NEWS",
                                            "url": "https://preview.colorlib.com/theme/dreams/blog.html"
                                        },
                                        {
                                            "text": "CONTACT",
                                            "url": "https://preview.colorlib.com/theme/dreams/contact.html"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "navright": [
                                {
                                    "icon": "fa fa-search search-switch",
                                    "klik": {
                                        "true": {
                                            "icon": "search-close-switch",
                                            "placeholder": "search here"
                                        }
                                    }
                                },
                                {
                                    "icon": "fa fa-facebook",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                },
                                {
                                    "icon": "fa fa-twitter",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                },
                                {
                                    "icon": "fa fa-instagram",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                },
                                {
                                    "icon": "fa fa-dribbble",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                },
                                {
                                    "text": "Get Started",
                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                }
                            ]
                        }
                    ]
                }
        elif element == 'body':
            if(args.jenisElement != None and args.jenisElement == 'body'):
                if(args.element != None and args.element == 'breadecrum'):
                    return{
                        "breadecrum": [
                            {
                                "bread1": {
                                    "url": "https://preview.colorlib.com/theme/dreams/#",
                                    "icon": "fa fa-home",
                                    "text": "Home"
                                },
                                "bread2": {
                                    "text": "Courses"
                                }
                            }
                        ]
                    }
                elif(args.element != None and args.element == 'application-form'):
                    return{
                        "aplication-form": [
                            {
                                "aplication-title": {
                                    "text1": "Giving Best Options For You",
                                    "text2": "Application Form"
                                },
                                "Form-application": [
                                    {
                                        "col-1": {
                                            "placeholder": "Your Name"
                                        },
                                        "col-2": {
                                            "placeholder": "Your Email"
                                        },
                                        "col-3": {
                                            "placeholder": "Your Phone"
                                        },
                                        "col-4": {
                                            "placeholder": "Date & time"
                                        },
                                        "col-5": [
                                            {
                                                "optional": {
                                                    "option1": "Courses type",
                                                    "option2": "Safe driving courses",
                                                    "option3": "motorhome Drivers"
                                                },
                                                "select-option": {
                                                    "option": "Courses type",
                                                    "list": {
                                                        "list1": "Courses type",
                                                        "list2": "safe driving courses",
                                                        "list3": "Motorhome drivers"
                                                    }
                                                }
                                            }
                                        ],
                                        "col-6": [
                                            {
                                                "optional": {
                                                    "option1": "Car type",
                                                    "option2": "hatcback",
                                                    "option3": "Sedan",
                                                    "option4": "Crossover"
                                                },
                                                "select-option": {
                                                    "option": "Car type",
                                                    "list": {
                                                        "list1": "Car type",
                                                        "list2": "Sedan",
                                                        "list3": "Crossover"
                                                    }
                                                }
                                            }
                                        ],
                                        "button": {
                                            "text": "SEND INQUIRY"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                else:
                    return{
                        "courses spad": [
                            {
                                "courses-title": [
                                    {
                                        "left": {
                                            "title": {
                                                "text1": "Our great Team",
                                                "text2": "Our instructor"
                                            }
                                        },
                                        "right": {
                                            "button": {
                                                "text": "View all"
                                            }
                                        }
                                    }
                                ],
                                "courses-item": [
                                    {
                                        "col-1": {
                                            "item-top": {
                                                "img": "img/courses/course-1.jpg",
                                                "text": "Winter driving",
                                                "price": "$ 119"
                                            },
                                            "item-buttom": [
                                                {
                                                    "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                                },
                                                {
                                                    "button": {
                                                        "url": "#",
                                                        "text": "View detail"
                                                    }
                                                }
                                            ]
                                        },
                                        "col-2": {
                                            "item-top": {
                                                "img": "img/courses/course-2.jpg",
                                                "text": "Programa for seniors",
                                                "price": "$ 119"
                                            },
                                            "item-buttom": [
                                                {
                                                    "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                                },
                                                {
                                                    "button": {
                                                        "url": "#",
                                                        "text": "View detail"
                                                    }
                                                }
                                            ]
                                        },
                                        "col-3": {
                                            "item-top": {
                                                "img": "img/courses/course-3.jpg",
                                                "text": "Adult in car lesons",
                                                "price": "$ 119"
                                            },
                                            "item-buttom": [
                                                {
                                                    "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                                },
                                                {
                                                    "button": {
                                                        "url": "#",
                                                        "text": "View detail"
                                                    }
                                                }
                                            ]
                                        },
                                        "col-4": {
                                            "item-top": {
                                                "img": "img/courses/course-4.jpg",
                                                "text": "Teen driver education",
                                                "price": "$ 119"
                                            },
                                            "item-buttom": [
                                                {
                                                    "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                                },
                                                {
                                                    "button": {
                                                        "url": "#",
                                                        "text": "View detail"
                                                    }
                                                }
                                            ]
                                        },
                                        "col-5": {
                                            "item-top": {
                                                "img": "img/courses/course-5.jpg",
                                                "text": "Defensive Driving",
                                                "price": "$ 119"
                                            },
                                            "item-buttom": [
                                                {
                                                    "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                                },
                                                {
                                                    "button": {
                                                        "url": "#",
                                                        "text": "View detail"
                                                    }
                                                }
                                            ]
                                        },
                                        "col-6": {
                                            "item-top": {
                                                "img": "img/courses/course-6.jpg",
                                                "text": "Stick shit lessons",
                                                "price": "$ 119"
                                            },
                                            "item-buttom": [
                                                {
                                                    "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt lacus"
                                                },
                                                {
                                                    "button": {
                                                        "url": "#",
                                                        "text": "View detail"
                                                    }
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        ]
                    }
            else:
                return {
                    "body": [
                        {
                            "hero_benner": {
                                "bacground_image": "img/hero-bg.jpg",
                                "hero_text": [
                                    {
                                        "text1": "BEST OPTIONS FOR YOU",
                                        "text2": "DRIVE SAFE & GET LICENSE",
                                        "hero_text_pilih": [
                                            {
                                                "text": "Contact Us",
                                                "url": "https://preview.colorlib.com/theme/dreams/#"
                                            },
                                            {
                                                "text": "See Courses",
                                                "url": "https://preview.colorlib.com/theme/dreams/#"
                                            }
                                        ]
                                    }
                                ]
                            },
                            "feature": [
                                {
                                    "feactur_text": {
                                        "text1": "Why choose us ?",
                                        "text2": "Our feature",
                                        "paragraf": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua viverra maecenas facilisis"
                                    }
                                },
                                {
                                    "feactur_item": [
                                        {
                                            "item1": {
                                                "img": "img/feature/xfeature-1.png.pagespeed.ic.22dCgiNvOu.webp",
                                                "text": "Unlimited Car Support"
                                            },
                                            "item2": {
                                                "img": "img/feature/xfeature-2.png.pagespeed.ic.r1evg5EssL.webp",
                                                "text": "Driving School Insures"
                                            },
                                            "item3": {
                                                "img": "img/feature/xfeature-3.png.pagespeed.ic.ZNUFBwu5wI.webp",
                                                "text": "Any Time Any Location"
                                            }
                                        }
                                    ]
                                }
                            ],
                            "about-vidio": [
                                {
                                    "vidio": {
                                        "img-bacground-vidio": "img/video-bg.jpg",
                                        "button": "btn play-vidio",
                                        "url-youtobe": "https://www.youtube.com/watch?v=bGuHgRQSEuk"
                                    },
                                    "about_vidio_text": [
                                        {
                                            "title": {
                                                "text1": "Welcome to Online trafic school",
                                                "text2": "looking for lessons?"
                                            },
                                            "paragraf": {
                                                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt utlabore et dolore magna aliqua. Quis ipsum vidnas accumsan lacus velfacilisis.",
                                                "button": {
                                                    "text": "Learn more",
                                                    "url": "https://preview.colorlib.com/theme/dreams/#"
                                                }
                                            }
                                        }
                                    ]
                                }
                            ],
                            "application-form": [
                                {
                                    "title": {
                                        "text1": "Giving Best Option For You",
                                        "text2": "Application Form"
                                    },
                                    "formulir": [
                                        {
                                            "input1": {
                                                "placeholder": "Your name"
                                            },
                                            "input2": {
                                                "placeholder": "Your Email"
                                            },
                                            "input3": {
                                                "placeholder": "Your Phone"
                                            },
                                            "input5": {
                                                "placeholder": "Date & time"
                                            },
                                            "option-item1": [
                                                {
                                                    "options": {
                                                        "option1": "Courses type",
                                                        "option2": "Safe Driving Courses",
                                                        "option3": "Motorhome Drivers"
                                                    },
                                                    "list": {
                                                        "list1": "Courses type",
                                                        "list2": "Safe Driving Courses",
                                                        "list3": "Motorhome Drivers"
                                                    }
                                                }
                                            ],
                                            "option-item2": [
                                                {
                                                    "options": {
                                                        "option1": "Car type",
                                                        "option2": "Hatcback",
                                                        "option3": "Sedan"
                                                    },
                                                    "list": {
                                                        "list1": "Car type",
                                                        "list2": "Hatcback",
                                                        "list3": "Sedan"
                                                    }
                                                }
                                            ],
                                            "button-send": {
                                                "text": "SEND INQUIRY"
                                            }
                                        }
                                    ]
                                }
                            ],
                            "pricing": [
                                {
                                    "pricing-title": {
                                        "text1": "Get Spesial Offer",
                                        "text2": "Our Pricing"
                                    },
                                    "pricing-item1": [
                                        {
                                            "text-top": "20% off",
                                            "price": "$ 199",
                                            "text": "Personal Driving"
                                        },
                                        {
                                            "list-item-pricing": {
                                                "list1": "Full course theory",
                                                "list2": "Full driving course",
                                                "list3": "Training in first aid",
                                                "list4": "Practical sessions",
                                                "list5": "Psychological support"
                                            }
                                        },
                                        {
                                            "text": "GET STARTED",
                                            "url": "https://preview.colorlib.com/theme/dreams/#"
                                        }
                                    ],
                                    "pricing-item2": [
                                        {
                                            "text-top": "20% off",
                                            "price": "$ 379",
                                            "text": "Power Booster"
                                        },
                                        {
                                            "list-item-pricing": {
                                                "list1": "Full course theory",
                                                "list2": "Full driving course",
                                                "list3": "Training in first aid",
                                                "list4": "Practical sessions",
                                                "list5": "Psychological support"
                                            }
                                        },
                                        {
                                            "text": "GET STARTED",
                                            "url": "https://preview.colorlib.com/theme/dreams/#"
                                        }
                                    ],
                                    "pricing-item3": [
                                        {
                                            "text-top": "20% off",
                                            "price": "$ 259",
                                            "text": "Freight Driving"
                                        },
                                        {
                                            "list-item-pricing": {
                                                "list1": "Full course theory",
                                                "list2": "Full driving course",
                                                "list3": "Training in first aid",
                                                "list4": "Practical sessions",
                                                "list5": "Psychological support"
                                            }
                                        },
                                        {
                                            "text": "GET STARTED",
                                            "url": "https://preview.colorlib.com/theme/dreams/?#"
                                        }
                                    ]
                                }
                            ],
                            "team": [
                                {
                                    "team-title": {
                                        "text1": "Our Great Team",
                                        "text2": "Our Instructor",
                                        "btn-team-all": {
                                            "text": "View all",
                                            "url": "https://preview.colorlib.com/theme/dreams/#"
                                        }
                                    },
                                    "team-item": [
                                        {
                                            "team-item1": [
                                                {
                                                    "item-img": {
                                                        "img": "img/team/xteam-1.png.pagespeed.ic.cHiltCofrK.webp"
                                                    },
                                                    "item-text": {
                                                        "text1": "DAVID WARNER",
                                                        "text2": "Instructor",
                                                        "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                    },
                                                    "item-social": {
                                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                                        "icon": {
                                                            "icon1": "fa fa-fecebook",
                                                            "icon2": "fa fa-twitter",
                                                            "icon3": "fa fa-instagram",
                                                            "icon4": "fa fa-dribbble"
                                                        }
                                                    }
                                                }
                                            ],
                                            "team-item2": [
                                                {
                                                    "item-img": {
                                                        "img": "img/team/xteam-2.png.pagespeed.ic.dZB3yfmD0i.webp"
                                                    },
                                                    "item-text": {
                                                        "text1": "DAVID WARNER",
                                                        "text2": "Instructor",
                                                        "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                    },
                                                    "item-social": {
                                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                                        "icon": {
                                                            "icon1": "fa fa-fecebook",
                                                            "icon2": "fa fa-twitter",
                                                            "icon3": "fa fa-instagram",
                                                            "icon4": "fa fa-dribbble"
                                                        }
                                                    }
                                                }
                                            ],
                                            "team-item3": [
                                                {
                                                    "item-img": {
                                                        "img": "img/team/xteam-3.png.pagespeed.ic.AOhA2y9pBh.webp"
                                                    },
                                                    "item-text": {
                                                        "text1": "DAVID WARNER",
                                                        "text2": "Instructor",
                                                        "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                    },
                                                    "item-social": {
                                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                                        "icon": {
                                                            "icon1": "fa fa-fecebook",
                                                            "icon2": "fa fa-twitter",
                                                            "icon3": "fa fa-instagram",
                                                            "icon4": "fa fa-dribbble"
                                                        }
                                                    }
                                                }
                                            ],
                                            "team-item4": [
                                                {
                                                    "item-img": {
                                                        "img": "img/team/xteam-4.png.pagespeed.ic.x98B_rqu1y.webp"
                                                    },
                                                    "item-text": {
                                                        "text1": "DAVID WARNER",
                                                        "text2": "Instructor",
                                                        "text3": "Morbi accumsan ipsum velit. Nam nec tellus a odio tincidunt auctor."
                                                    },
                                                    "item-social": {
                                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                                        "icon": {
                                                            "icon1": "fa fa-fecebook",
                                                            "icon2": "fa fa-twitter",
                                                            "icon3": "fa fa-instagram",
                                                            "icon4": "fa fa-dribbble"
                                                        }
                                                    }
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                }
        elif element == 'footer':
            if(args.jenisElement != None and args.jenisElement == 'footer'):
                if(args.element != None and args.element == 'body-footer'):
                    return{
                        "body-footer": [
                            {
                                "footer-widget1": [
                                    {
                                        "title": {
                                            "text": "COMPANY"
                                        }
                                    },
                                    {
                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                        "list": {
                                            "list1": "About Us",
                                            "list2": "Company",
                                            "list3": "Press & blog",
                                            "list4": "Privacy Policy",
                                            "list5": "Faq"
                                        }
                                    }
                                ],
                                "footer-widget2": [
                                    {
                                        "title": {
                                            "text": "Courses"
                                        }
                                    },
                                    {
                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                        "list": {
                                            "list1": "Winter driving",
                                            "list2": "Program for seniors",
                                            "list3": "Adult in car lesons",
                                            "list4": "Defensive driving",
                                            "list5": "Stick shift lessons"
                                        }
                                    }
                                ],
                                "footer-widget3": [
                                    {
                                        "title": {
                                            "text": "USEFUL LINKS"
                                        }
                                    },
                                    {
                                        "url": "https://preview.colorlib.com/theme/dreams/#",
                                        "list": {
                                            "list1": "Home",
                                            "list2": "Drupal Themes",
                                            "list3": "Wordpress Themes",
                                            "list4": "Support",
                                            "list5": "Services"
                                        }
                                    }
                                ],
                                "footer-about": [
                                    {
                                        "logo": {
                                            "img": "img/xfooter-logo.png.pagespeed.ic.m_mZ4QWNCF.webp",
                                            "text": "Address : 15 Division Street, New York, NY 12032, United States of America"
                                        }
                                    },
                                    {
                                        "list": {
                                            "phone": "+0 (123) 456789",
                                            "Email": "kaseo@gmail.com",
                                            "Fax": "+8 (123) 456 789"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                else:
                    return{
                        "footer-finis": {
                            "text": "Copyright © 2022 All rights reserved | This template is made with",
                            "icon": "fa fa-heart",
                            "blank": {
                                "text": "Colorlib",
                                "url": "https://colorlib.com/"
                            }
                        }
                    }
            else:
                return {
                    "footer": [
                        {
                            "body-footer": [
                                {
                                    "footer-widget1": [
                                        {
                                            "title": {
                                                "text": "COMPANY"
                                            }
                                        },
                                        {
                                            "url": "https://preview.colorlib.com/theme/dreams/#",
                                            "list": {
                                                "list1": "About Us",
                                                "list2": "Company",
                                                "list3": "Press & blog",
                                                "list4": "Privacy Policy",
                                                "list5": "Faq"
                                            }
                                        }
                                    ],
                                    "footer-widget2": [
                                        {
                                            "title": {
                                                "text": "Courses"
                                            }
                                        },
                                        {
                                            "url": "https://preview.colorlib.com/theme/dreams/#",
                                            "list": {
                                                "list1": "Winter driving",
                                                "list2": "Program for seniors",
                                                "list3": "Adult in car lesons",
                                                "list4": "Defensive driving",
                                                "list5": "Stick shift lessons"
                                            }
                                        }
                                    ],
                                    "footer-widget3": [
                                        {
                                            "title": {
                                                "text": "USEFUL LINKS"
                                            }
                                        },
                                        {
                                            "url": "https://preview.colorlib.com/theme/dreams/#",
                                            "list": {
                                                "list1": "Home",
                                                "list2": "Drupal Themes",
                                                "list3": "Wordpress Themes",
                                                "list4": "Support",
                                                "list5": "Services"
                                            }
                                        }
                                    ],
                                    "footer-about": [
                                        {
                                            "logo": {
                                                "img": "img/xfooter-logo.png.pagespeed.ic.m_mZ4QWNCF.webp",
                                                "text": "Address : 15 Division Street, New York, NY 12032, United States of America"
                                            }
                                        },
                                        {
                                            "list": {
                                                "phone": "+0 (123) 456789",
                                                "Email": "kaseo@gmail.com",
                                                "Fax": "+8 (123) 456 789"
                                            }
                                        }
                                    ]
                                }
                            ],
                            "footer-finis": {
                                "text": "Copyright © 2022 All rights reserved | This template is made with",
                                "icon": "fa fa-heart",
                                "blank": {
                                    "text": "Colorlib",
                                    "url": "https://colorlib.com/"
                                }
                            }
                        }
                    ]
                }
        else:
            return "not found"


# Get untuk menu home
api.add_resource(Structure, '/api/v1/home/<string:element>/', )
api.add_resource(Home, '/api/v1/home/')

# Get menu courses
api.add_resource(Courses, '/api/v1/courses/')
api.add_resource(Bagian,'/api/v1/courses/<string:element>')


@app.route('/')
def index():
    return 'API Tutorials with Flask.eg /api/v1/home'


# Using JSONIFY ERROR
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
