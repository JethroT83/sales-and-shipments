import reactLogo from '@Assets/react.svg';
import djangoLogo from '@Assets/django-logo.webp';

export default function ApplicationLogo(props) {
    return (
        <div className="inline-flex items-center gap-6" {...props}>
            <img src={djangoLogo} alt="Django" className="h-16 w-16 object-contain inline-block" />
            <span className="text-3xl font-bold text-gray-700 px-2">+</span>
            <img src={reactLogo}  alt="React"  className="h-16 w-16 object-contain inline-block" />
        </div>
    );
}
